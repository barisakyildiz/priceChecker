import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pickle
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self, url):
        self.url = "https://www.wildberries.ru/catalog/16429349/detail.aspx?"
        self.PICKLES_PATH = 'pic.pkl'
        options = Options()
        options.headless = False
        options.page_load_strategy = 'eager'
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        DRIVER_PATH = '/home/da3rny/Tornacı/priceChecker/chromedriver'
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        self.action = webdriver.ActionChains(self.driver)
        self.driver.get(self.url)
        sleep(3)
        self.loadCookies(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(4000)
        self.element = self.driver.find_elements(by=By.CLASS_NAME, value='product-page__price-block')
        print("------------------------------------")
        print(self.element)
        print("------------------------------------")
        for element in self.element:
            try:
                self.action.move_to_element(element)
                self.action.perform()
                sleep(1)
            except Exception as e:
                print("NO SIZE AND SMT" + str(e))
                sleep(1)
        sleep(5)
        self.html = self.driver.page_source
        #print(self.html)
        print("------------------------------------")
        where = self.html.find("Скидка покупателя")
        print(self.html[where:where+60])
        print("------------------------------------")

    def dumpCookies(self, driver):
        with open(self.PICKLES_PATH, 'wb') as filehandler:
            pickle.dump(driver.get_cookies(), filehandler)
    
    def loadCookies(self, driver):
     with open(self.PICKLES_PATH, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
            del cookie["domain"]
            print(cookie)
            driver.add_cookie(cookie)
    
import sys
import os

dri = Driver("difugh")