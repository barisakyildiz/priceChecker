from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pickle

class Driver:
    def __init__(self, url):
        self.url = url
        options = Options()
        options.headless = True
        options.page_load_strategy = 'eager'
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        DRIVER_PATH = 'chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        self.driver.get(url)
        self.driver.maximize_window(); sleep(5)
        self.html = self.driver.page_source
        self.where = self.html.find("price-block__final-price")
        self.where_old = self.html.find("price-block__old-price j-wba-card-item-show")
        self.PICKLES_PATH = "pick.pkl"

    def findPrice(self):
        price = self.html[self.where:(self.where) + 60]
        price = price.replace('&nbsp', ''); price = price.replace(' ', ''); price = price.replace('price-block__final-price">', ''); price = price.replace(';', ' ')
        price = price.replace(' ', ''); price_integer = int(price.replace("₽", ''))
        return price, price_integer
    
    def findDiscount(self):
        discount = self.html[self.where_old:(self.where_old) + 310]; self.where_old = discount.find("&nbsp") - 4; discount = discount[self.where_old:]; discount = discount.replace(' ', '')
        discount = discount.replace('&nbsp', ''); discount = discount.replace(';', ' ')
        discount = discount.replace('</del>', ''); discont_integer = discount.replace(' ', ''); discont_integer = int(discont_integer.replace('₽', ''))
        self.driver.quit()
        return discount, discont_integer #returns not discount but old price

    def findPercentage(self, old_price, new_price):
        percentage = new_price / old_price; percentage = percentage * 100
        percentage = 100 - percentage
        return int(percentage)

    def dumpCookies(self, driver):
        with open(self.PICKLES_PATH, 'wb') as filehandler:
            pickle.dump(driver.get_cookies(), filehandler)
    
    def loadCookies(self, driver):
     with open(self.PICKLES_PATH, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
            driver.add_cookie(cookie)

def main():
    driver = Driver('https://www.wildberries.ru/catalog/16429349/detail.aspx?') #For Testing
    try:
        current_price, current_price_integer = driver.findPrice()
        old_price, old_price_integer = driver.findDiscount()
        percentage = (driver.findPercentage(old_price=old_price_integer, new_price=current_price_integer))
        print("\n\nOLD PRICE --> {}\n\n".format(old_price))
        print("PRICE --> {}\n\n".format(current_price))
        print("DISCOUNT PERCENTAGE --> {}%\n\n".format(str(percentage)))
    except:
        msg = "Item Out of Stock"
        print(msg)
    

if __name__ == '__main__':
    main()