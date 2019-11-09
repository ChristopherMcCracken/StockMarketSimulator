import requests
import json


# -------------------------------------------------------------------------------------------------------------------- #
def GrabDataFromAPI(ticker):

    # Grab data from API
    stockRequestAPI = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol=' + ticker + '&api_token=oL8qjdubhjFMONwfBVsJ0erhd73PVMmowP8z7TVwmRgUxpHoSB4iNDJ3Jj0y')

    # Convert JSON to Dict
    stockRequestJSON = stockRequestAPI.text
    stockRequestDict = json.loads(stockRequestJSON)

    # print(stockRequestDict)

    # Grab data from Dict
    stockName = stockRequestDict['data'][0]['name']
    stockSymbol = stockRequestDict['data'][0]['symbol']
    stockPrice = stockRequestDict['data'][0]['price']
    lastUpdatedTime = stockRequestDict['data'][0]['last_trade_time']
    print(f'{stockName} ({stockSymbol}): ${stockPrice}, last updated at {lastUpdatedTime}\n')

    return stockRequestDict
# -------------------------------------------------------------------------------------------------------------------- #
