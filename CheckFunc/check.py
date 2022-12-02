import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

class FileOp:
    def __init__(self):
        self.url_file_name = "producturls.csv"
        self.prices_file_name = "prices.csv"
        self.SAVE_TO_CSV = True
        self.PRICES_CSV = "prices.csv"
        self.url = ""
    
    def getFromUrl(self):
        url_dataframe = pd.read_csv(self.url_file_name)
        return url_dataframe
    
    def processProd(self):
        updated = []
        dataframe = self.getFromUrl()
        for prod in dataframe.to_dict("records"):
            webop = WebOp(prod["url"])
            html = webop.getHTML(prod["url"])
            prod["price"] = webop.returnPrice(html)
            prod["alert"] = prod["price"] < prod["alert_price"]
            updated.append(prod)
            del webop
        return pd.DataFrame(updated)

class WebOp:
    def __init__(self, url):
        self.url = url
    
    def getHTML(self, url):
        html = requests.get(url)
        return html.text
    
    def returnPrice(self, html):
        s = BeautifulSoup(html, "lxml")
        el = s.select_one(".price_color") #CHANGE FOR WILDBERRIES
        price = Price.fromstring(el.text)
        return price.amount_float

def main():
    pass

if __name__ == '__main__':
    main()