import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

class FileOp:
    def __init__(self):
        self.url_file_name = "producturls.csv"
        self.prices_file_name = "prices.csv"
        self.SAVE_TO_CSV = True
    
    def getFromUrl(self, csv):
        url_dataframe = pd.read_csv(csv)
        return url_dataframe
    
    def processProd(self, dataframe):
        for prod in dataframe.to_dict("records"):
            pass #will be back


def main():
    pass

if __name__ == '__main__':
    main()