import pandas as pd
import driver
import telegram
from os import system

class FileOp:
    def __init__(self):
        self.url_docx_name = "dataset.txt"
        self.prices_file_name = "prices.csv"
        self.SAVE_TO_CSV = True
        self.PRICES_CSV = "prices.csv"
        self.url = ""
        self.SEND_NOTIFICATION = False
    
    def readFromDoc(self):
        temp_total_code = []; temp = []; temp_total_full = []; temp2 = []
        with open(self.url_docx_name, encoding="utf-8") as f:
            lines = f.readlines()
        for string in lines:
            if string != '\n':
                temp2.append(string)
                for t in string.split():
                    try:
                        temp.append(int(t))
                    except ValueError:
                        pass
            elif string == '\n':
                temp_total_code.append(temp)
                temp_total_full.append(temp2)
                temp = []
                temp2 = []
        for prod_group in temp_total_full:
            for prod in prod_group:
                prod_group[prod_group.index(prod)] = prod.replace('\n', '')
        f.close()
        return temp_total_code, temp_total_full
    
    def createLinks(self):
        arr, _ = self.readFromDoc(); temp = []; temp_total = []
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                string_temp = 'https://www.wildberries.ru/catalog/' + str(arr[i][j]) + '/detail.aspx?'
                temp.append(string_temp)
            temp_total.append(temp); temp = []
        return temp_total, _
    
    def writeToCSV(self):
        old_df = self.getFromUrl(); old_df = old_df.to_dict(); old_counter = 0
        arr, _ = self.createLinks(); updated = []; dicti = {}; group_number = 0
        if self.SAVE_TO_CSV:
            for prod_group in arr:
                for prod in prod_group:
                    old_price = int(old_df["discounted_price"][old_counter])
                    print("\n\nCURRENT URL --> {}\n\n".format(prod))
                    dri = driver.Driver(str(prod))
                    dicti["name"] = _[group_number][prod_group.index(prod)]
                    try:
                        discounted_price = (dri.findPrice())[1]; price = (dri.findDiscount())[1]
                        if int(discounted_price) != int(old_price):
                            self.SEND_NOTIFICATION = True #test et print ekleyerek
                        dicti["price"] = price
                        dicti["discounted_price"] = discounted_price
                        dicti["discount_percentage"] = dri.findPercentage(price, discounted_price)
                    except ValueError as e:
                        dicti["price"] = "OUT OF STOCK"
                        dicti["discounted_price"] = "OUT OF STOCK"
                        dicti["discount_percentage"] = "OUT OF STOCK"
                        print(str(e) + ": Item is out of stock")
                    dicti["url"] = prod
                    dicti["group_number"] = group_number
                    print(dicti)
                    del dri
                    updated.append(dicti);
                    for i in range(1, 100):
                        if old_counter - i >= 0 and old_df["group_number"][old_counter] == old_df["group_number"][old_counter - i]:
                            pass
                        elif (old_counter - i <= 0) or (old_counter - i >= 0 and old_df["group_number"][old_counter] != old_df["group_number"][old_counter - i]):
                            minus = i - 1
                            break
                    if self.SEND_NOTIFICATION == True and minus != 0:
                        msg = telegram.createMessage(old_price, discounted_price, dicti["discount_percentage"], dicti["url"], dicti["name"], old_df["discounted_price"][old_counter - minus], old_df["discount_percentage"][old_counter - minus])
                        telegram.sendNot(msg=msg)
                    old_counter += 1
                    dicti = {}
                    self.SEND_NOTIFICATION = False
                    system("clear")
                group_number += 1
            df = pd.DataFrame(updated)
            df.to_csv(self.PRICES_CSV, mode="w")
            

    def getFromUrl(self):
        url_dataframe = pd.read_csv(self.prices_file_name)
        return url_dataframe


def main():
    fileop = FileOp()
    #fileop.readFromDoc()
    #print(fileop.readFromDoc2())
    #codes, fullarr = fileop.readFromDoc(); print(fullarr)
    fileop.writeToCSV()

if __name__ == '__main__':
    main()