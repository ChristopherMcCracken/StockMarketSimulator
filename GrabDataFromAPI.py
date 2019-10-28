import requests
import json


# -------------------------------------------------------------------------------------------------------------------- #
def GrabDataFromAPI(tickers):

    # Grab data from API
    # Add functionality to allow user to use their own token?
    stocksToRequest = ''
    for ticker in tickers:
        stocksToRequest += ',' + ticker

    stockRequestAPI = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol=' + stocksToRequest + '&api_token=oL8qjdubhjFMONwfBVsJ0erhd73PVMmowP8z7TVwmRgUxpHoSB4iNDJ3Jj0y')

    # Convert JSON to Dict
    stockRequestJSON = stockRequestAPI.text
    stockRequestDict = json.loads(stockRequestJSON)

    # print(stockRequestDict)

    # Grab data from Dict
    for i in range(len(tickers)):
        stockName = stockRequestDict['data'][i]['name']
        stockSymbol = stockRequestDict['data'][i]['symbol']
        stockPrice = stockRequestDict['data'][i]['price']
        lastUpdatedTime = stockRequestDict['data'][i]['last_trade_time']
        print(f'{stockName} ({stockSymbol}): ${stockPrice}, last updated at {lastUpdatedTime}\n')

    return stockRequestDict
# -------------------------------------------------------------------------------------------------------------------- #
