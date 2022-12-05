import pandas as pd
import driver

class FileOp:
    def __init__(self):
        self.url_docx_name = "dataset.docx"
        self.url_file_name = "producturls.csv"
        self.prices_file_name = "prices.csv"
        self.SAVE_TO_CSV = True
        self.PRICES_CSV = "prices.csv"
        self.url = ""
    
    def readFromDoc(self):
        temp_total_code = []; temp = []; temp_total_full = []; temp2 = []
        with open('dataset.txt', encoding="utf-8") as f:
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
        arr, _ = self.createLinks(); updated = []; dicti = {}; group_number = 0
        if self.SAVE_TO_CSV:
            print(arr)
            for prod_group in arr:
                for prod in prod_group:
                    print("\n\nCURRENT URL --> {}\n\n".format(prod))
                    dri = driver.Driver(str(prod))
                    dicti["name"] = _[group_number][prod_group.index(prod)]
                    try:
                        discounted_price = (dri.findPrice())[1]; price = (dri.findDiscount())[1]
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
                    updated.append(dicti); dicti = {}
                group_number += 1
            df = pd.DataFrame(updated)
            df.to_csv(self.PRICES_CSV, mode="w")
            

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


def main():
    fileop = FileOp()
    #fileop.readFromDoc()
    #print(fileop.readFromDoc2())
    #codes, fullarr = fileop.readFromDoc(); print(fullarr)
    fileop.writeToCSV()

if __name__ == '__main__':
    main()