from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pickle
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self, url):
        self.url = url
        self.PICKLES_PATH = 'pic.pkl'
        options = Options()
        options.headless = False
        options.page_load_strategy = 'eager'
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        DRIVER_PATH = '/home/da3rny/Tornacı/priceChecker/chromedriver'
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        self.action = webdriver.ActionChains(self.driver)
        self.driver.get(url); sleep(3)
        self.loadCookies(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window(); sleep(10)
        self.element = self.driver.find_elements(by=By.CLASS_NAME, value='price-block__content')
        print(self.element)
        for element in self.element:
            try:
                self.action.move_to_element(element)
                self.action.move_by_offset(-15, 0)
                self.action.perform()
                sleep(2)
                break;
            except Exception as e:
                print("NO SIZE AND SMT")
                sleep(1)
        self.html = self.driver.page_source
        self.where = self.html.find("price-block__final-price")
        self.where_old = self.html.find("price-block__old-price j-wba-card-item-show")
        self.where_without_discount = self.html.find("Скидка") + 40
        self.where_percentage = self.html.find("Скидка покупателя")

    def KeKePercentage(self):
        perc = self.html[self.where_percentage:self.where_percentage + 60]
        perc = perc.replace('Скидка покупателя', ''); perc = perc.replace(' ', '')
        perc = perc.replace('<spanclass="discoun', ''); perc = perc.replace('%</span>', '')
        try:
            return(int(perc))
        except Exception as e:
            return "NO DISCOUNT"

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
    
    def notDiscountPrice(self):
        price = self.html[self.where_without_discount:self.where_without_discount + 40]
        price = price.replace('"discount-tooltipster-value">', ''); price = price.replace('&nbsp;₽', ''); price = price.replace('=', '')
        price = price.replace('&nbsp;', '')
        try:
            return int(price)
        except Exception as e:
            return "NO DISCOUNTED PRICE"

    def dumpCookies(self, driver):
        with open(self.PICKLES_PATH, 'wb') as filehandler:
            pickle.dump(driver.get_cookies(), filehandler)
    
    def loadCookies(self, driver):
     with open(self.PICKLES_PATH, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
            del cookie["domain"]
            driver.add_cookie(cookie)

def main():
    driver = Driver('https://www.wildberries.ru/catalog/14057934/detail.aspx?') #For Testing
    current_price, current_price_integer = driver.findPrice()
    old_price, old_price_integer = driver.findDiscount()
    percentage = (driver.findPercentage(old_price=old_price_integer, new_price=current_price_integer))
    not_disc = driver.notDiscountPrice()
    perc = driver.KeKePercentage()
    print("\n\nOLD PRICE --> {}\n\n".format(old_price))
    print("PRICE --> {}\n\n".format(current_price))
    print("DISCOUNT PERCENTAGE --> {}%\n\n".format(str(percentage)))
    print("KEKE PERCENTAGE --> {}%\n\n".format(perc))
    print("WITHOUT DISC --> {}\n\n".format(not_disc))
    

if __name__ == '__main__':
    main()