from CheckFunc import check

def main():
    checkobj = check.FileOp()
    dataframe_updated = checkobj.processProd()
    if checkobj.SAVE_TO_CSV:
        dataframe_updated.to_csv(checkobj.PRICES_CSV, mode="a")

if __name__ == '__main__':
    main()