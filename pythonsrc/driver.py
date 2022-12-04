from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class Driver:
    def __init__(self, url):
        self.url = url
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        DRIVER_PATH = 'chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        self.driver.get(url)
        self.driver.maximize_window(); sleep(5)
        self.html = self.driver.page_source
        self.where = self.html.find("price-block__final-price")
        self.where_old = self.html.find("price-block__old-price j-wba-card-item-show")
    
    def findPrice(self):
        price = self.html[self.where:(self.where) + 60]
        price = price.replace('&nbsp', ''); price = price.replace(' ', ''); price = price.replace('price-block__final-price">', ''); price = price.replace(';', ' ')
        price_integer = int(price.replace(" ₽", ''))
        return price, price_integer
    
    def findDiscount(self):
        discount = self.html[self.where_old:(self.where_old) + 300]; self.where_old = discount.find("&nbsp") - 4; discount = discount[self.where_old:]; discount = discount.replace(' ', '')
        discount = discount.replace('&nbsp', ''); discount = discount.replace(';', ' ')
        discont_integer = discount.replace(' ', ''); discont_integer = int(discont_integer.replace('₽', ''))
        self.driver.quit()
        return discount, discont_integer #returns not discount but old price

    def findPercentage(self, old_price, new_price):
        percentage = new_price / old_price; percentage = percentage * 100
        return int(percentage)

def main():
    driver = Driver('https://www.wildberries.ru/catalog/16429345/detail.aspx?') #For Testing
    try:
        current_price, current_price_integer = driver.findPrice()
        old_price, old_price_integer = driver.findDiscount()
        percentage = 100 - (driver.findPercentage(old_price=old_price_integer, new_price=current_price_integer))
        print("\n\nOLD PRICE --> {}\n\n".format(old_price))
        print("PRICE --> {}\n\n".format(current_price))
        print("DISCOUNT PERCENTAGE --> {}%\n\n".format(str(percentage)))
    except Exception as e:
        msg = "Item Out of Stock"
        print(msg)
    

if __name__ == '__main__':
    main()