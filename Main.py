from Portfolio import Portfolio
from GrabDataFromAPI import GrabDataFromAPI
from SQLite import insertPortfolio, loadPortfolioFromDB
from tabulate import tabulate


# -------------------------------------------------------------------------------------------------------------------- #
def buySellStocks(name, stockTicker, stockAmount, tickerPrice):
    amountSpent = float(stockAmount) * tickerPrice
    if stockAmount < 0 and (abs(stockAmount) > Portfolio.portfolios[name]['Stocks'][stockTicker]):
        return

    if stockTicker in Portfolio.portfolios[name]['Stocks']:
        Portfolio.portfolios[name]['Stocks'][stockTicker] += stockAmount
    else:
        Portfolio.portfolios[name]['Stocks'][stockTicker] = stockAmount
    insertPortfolio(name)  # update portfolio in db

    print(f'\nYou have spent {amountSpent} for {stockAmount} shares of {stockTicker}\n')
    Portfolio.portfolios[name]['Overview']['sharesOwned'] += stockAmount
    Portfolio.portfolios[name]['Overview']['netSpent'] += amountSpent

# -------------------------------------------------------------------------------------------------------------------- #
def getStockPrice(name, stockTicker):
    try:
        Portfolio.portfolios[name]
    except:
        loadPortfolioFromDB(name)

    print(stockTicker)
    stockData = GrabDataFromAPI(stockTicker)
    print(stockData)
    tickerPrice = float(stockData['data'][0]['price'])
    print(f"The price of this ticker is: {tickerPrice}")
    return tickerPrice


# -------------------------------------------------------------------------------------------------------------------- #
def getAllStockData(stockTickers):
    stockRequestDict = GrabDataFromAPI(stockTickers)
    table = []
    for i in stockRequestDict['data']:
        for key, value in i.items():
            table.append([str(key) + ':', str(value)])
    return str(tabulate(table))

# -------------------------------------------------------------------------------------------------------------------- #
def getPortfolioInfo(name):
    # Check if portfolio with name sent in is already loaded into program, if not, try to load it from database
    try:
        Portfolio.portfolios[name]
    except:
        loadPortfolioFromDB(name)

    if Portfolio.portfolios[name]['Stocks']:  # if there are no stocks bought yet, the dictionary evaluates to false and passes this block
        stockList = list(Portfolio.portfolios[name]['Stocks'])  # cast to list to be able to access stocks by integer index
        stockData = GrabDataFromAPI(stockList)
        amountSpent = 0
        i = 0
        print(f"STOCK DATA: {stockData}")
        for stock in sorted(Portfolio.portfolios[name]['Stocks']):  # stock data and Portfolio are now iterated in abc order
            print(f"STOCK: {stock}")
            tickerPrice = float(stockData['data'][i]['price'])
            i += 1
            stockAmount = Portfolio.portfolios[name]['Stocks'][stock]
            print(f"tickerPrice: {tickerPrice}")
            print(f"stockAmount: {stockAmount}")
            amountSpent += stockAmount * tickerPrice
            print(f"amountSpent: {amountSpent}")
        Portfolio.portfolios[name]['Overview']['netWorth'] = amountSpent
        Portfolio.portfolios[name]['Overview']['netGainLoss'] = Portfolio.portfolios[name]['Overview']['netWorth'] - Portfolio.portfolios[name]['Overview']['netSpent']

    insertPortfolio(name)  # update portfolio in db

    table = [
        ['Name:', Portfolio.portfolios[name]['Overview']['Name']],
        ['Net Spent:', '$' + str(Portfolio.portfolios[name]['Overview']['netSpent'])],
        ['Net Worth:', '$' + str(Portfolio.portfolios[name]['Overview']['netWorth'])],
        ['Net Gain/Loss:', '$' + str(Portfolio.portfolios[name]['Overview']['netGainLoss'])],
        ['Shares Owned:', str(Portfolio.portfolios[name]['Overview']['sharesOwned']) + ' Shares']
    ]

    if Portfolio.portfolios[name]['Overview']['netSpent'] != 0:
        table.insert(4, ['Percent Gain/Loss:', str((Portfolio.portfolios[name]['Overview']['netWorth'] -
                                             Portfolio.portfolios[name]['Overview']['netSpent']) /
                                             Portfolio.portfolios[name]['Overview']['netSpent'] * 100) + '%'])
    for key, value in Portfolio.portfolios[name]['Stocks'].items():
        table.append([str(key) + ':', str(value) + " Shares"])
    print(str(tabulate(table)))
    return str(tabulate(table))


# -------------------------------------------------------------------------------------------------------------------- #
def createPortfolio(name):
    newPortfolio = Portfolio({'Overview': {'Name': name,  'sharesOwned': 0, 'netWorth': 0, 'netSpent': 0, 'netGainLoss': 0},
                              'Stocks': {}})
    insertPortfolio(name)  # save portfolio to db
    return newPortfolio


# -------------------------------------------------------------------------------------------------------------------- #
# Default Portfolio
Portfolio({'Overview': {'Name': 'Default',  'sharesOwned': 0, 'netWorth': 0, 'netSpent': 0, 'netGainLoss': 0},
           'Stocks': {}})

# -------------------------------------------------------------------------------------------------------------------- #
