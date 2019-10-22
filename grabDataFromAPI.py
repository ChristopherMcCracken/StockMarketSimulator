import requests
import json

# -------------------------------------------------------------------------------------------------------------------- #
tickers = ['AMD', 'INTC', 'NVDA']

# Grab data from API
stockRequestAPI = requests.get('https://api.worldtradingdata.com/api/v1/stock?symbol='
                               + tickers[0] + ',' + tickers[1] + ',' + tickers[2] +
                               '&api_token=oL8qjdubhjFMONwfBVsJ0erhd73PVMmowP8z7TVwmRgUxpHoSB4iNDJ3Jj0y')

# Convert JSON to Dict
stockRequestJSON = stockRequestAPI.text
stockRequestDict = json.loads(stockRequestJSON)

print(stockRequestDict)

# Grab data from Dict
for i in range(len(tickers)):
    stockName = stockRequestDict['data'][i]['name']
    stockSymbol = stockRequestDict['data'][i]['symbol']
    stockPrice = stockRequestDict['data'][i]['price']
    lastUpdatedTime = stockRequestDict['data'][i]['last_trade_time']
    print(f'{stockName} ({stockSymbol}): ${stockPrice}, last updated at {lastUpdatedTime}')
# -------------------------------------------------------------------------------------------------------------------- #
