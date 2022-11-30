import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

class FileOp:
    def __init__(self):
        self.url_file_name = "producturls.csv"
        self.prices_file_name = "prices.csv"
        self.SAVE_TO_CSV = True
    
    def get_from_url(self, csv):
        url_dataframe = pd.read_csv(csv)
        

def main():
    pass

if __name__ == '__main__':
    main()