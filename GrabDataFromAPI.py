import numpy as np
import requests
import json


# -------------------------------------------------------------------------------------------------------------------- #
def GrabDataFromAPI(tickers):

    # Grab data from API
    stocksToRequest = ''
    if type(tickers) is list:
        for ticker in tickers:
            print(ticker)
            stocksToRequest += ',' + ticker
    else:
        stocksToRequest = tickers

    # despite order sent in, api returns data in abc order
    stockRequestAPI = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol=' + stocksToRequest + '&api_token=oL8qjdubhjFMONwfBVsJ0erhd73PVMmowP8z7TVwmRgUxpHoSB4iNDJ3Jj0y')

    # Convert JSON to Dict
    stockRequestJSON = stockRequestAPI.text
    stockRequestDict = json.loads(stockRequestJSON)
    print(stockRequestDict)
    # Grab data from Dict
    if type(tickers) is list:
        for i in range(len(tickers)):
            stockName = stockRequestDict['data'][i]['name']
            stockSymbol = stockRequestDict['data'][i]['symbol']
            stockPrice = stockRequestDict['data'][i]['price']
            lastUpdatedTime = stockRequestDict['data'][i]['last_trade_time']
            print(f'{stockName} ({stockSymbol}): ${stockPrice}, last updated at {lastUpdatedTime}\n')
    else:
        stockName = stockRequestDict['data'][0]['name']
        stockSymbol = stockRequestDict['data'][0]['symbol']
        stockPrice = stockRequestDict['data'][0]['price']
        lastUpdatedTime = stockRequestDict['data'][0]['last_trade_time']
        print(f'{stockName} ({stockSymbol}): ${stockPrice}, last updated at {lastUpdatedTime}\n')

    return stockRequestDict


# -------------------------------------------------------------------------------------------------------------------- #
def grabStockHistory(ticker, amountOfDays):
    stockRequest = requests.get('https://api.worldtradingdata.com/api/v1/history?symbol=' + ticker + '&sort=newest&api_token=oL8qjdubhjFMONwfBVsJ0erhd73PVMmowP8z7TVwmRgUxpHoSB4iNDJ3Jj0y')
    stockRequestJSON = stockRequest.text
    stockRequestDict = json.loads(stockRequestJSON)

    rows, cols = (amountOfDays, 5)
    data = [['' for i in range(cols)] for j in range(rows)]

    for index, date in enumerate(stockRequestDict['history']):
        # print(stockRequestDict['history'][date]['close'])
        data[index][0] = date  # fix this to date
        data[index][1] = stockRequestDict['history'][date]['open']
        data[index][2] = stockRequestDict['history'][date]['high']
        data[index][3] = stockRequestDict['history'][date]['low']
        data[index][4] = stockRequestDict['history'][date]['close']
        if index == amountOfDays-1:
            break

    return data
