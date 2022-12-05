from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Driver:
    def __init__(self, url):
        self.url = "https://www.wildberries.ru/catalog/16429349/detail.aspx?"
        options = Options()
        options.headless = True
        options.page_load_strategy = 'eager'
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        DRIVER_PATH = 'chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        self.driver.get(self.url)
        self.driver.maximize_window(); sleep(5)
        self.html = self.driver.page_source
        print(self.html)
    
dri = Driver("difugh")