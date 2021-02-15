import json
import urllib.request
import pandas as pd

symbol = ""
should_continue = True

def getStockData(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=HUMW752VA1NVSU2T'
    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()
    data = json.loads(responseString)
    df = data['Time Series (Daily)']
    prices = pd.DataFrame.from_dict(df)
    closing_price = prices.iloc[3, 0]
    
    return closing_price

            

def main():
    save_file = open('japi.out', 'w')
    while should_continue:
        symbol = input("Enter Stock Symbol or EXIT to exit: ").upper()

        if symbol != "EXIT":
            stock_price = 'The current price of {} is: {}'.format(symbol, getStockData(symbol))        
            print(stock_price)
            save_file.write(stock_price)
            
        else:
            print('Goodbye')
            break
            
        
main()
