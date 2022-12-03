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
            print("BEFORE ---> " + str(prod))
            webop = WebOp(prod["url"])
            html = webop.getHTML(prod["url"])
            prod["price"] = webop.returnPrice(html)
            prod["alert"] = prod["price"] < prod["alert_price"]
            updated.append(prod)
            print("AFTER ---> " + str(prod) + "\n\n")
            del webop
        return pd.DataFrame(updated)

class WebOp:
    def __init__(self, url):
        self.url = url
    
    def getHTML(self, url):
        r_obj = requests.Session()
        r_soup = r_obj.get("https://www.wildberries.ru")
        return r_soup
    
    def returnPrice(self, html):
        soup = BeautifulSoup(html.content , "lxml")
        hidden_inputs = soup.find_all("price-block__final-price",type="hidden")
        url_needed = "aspx_endpoint"
        print("SOUP --> \n\n"+ str(soup) + "\n\n")
        el = soup.select_one(".price-block__price-wrap")
        print("EL --> \n\n"+ str(el) + "\n\n")
        price = Price.fromstring(el.text)
        return price.amount_float

def main():
    pass

if __name__ == '__main__':
    main()