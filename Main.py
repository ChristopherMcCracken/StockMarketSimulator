from Portfolio import Portfolio
from GrabDataFromAPI import GrabDataFromAPI
from SQLite import insertPortfolio, loadPortfolioFromDB


# -------------------------------------------------------------------------------------------------------------------- #
def buySellStocks(name, stockTicker, stockAmount):
    try:
        Portfolio.portfolios[name]
    except:
        loadPortfolioFromDB(name)

    print(stockTicker)
    stockData = GrabDataFromAPI(stockTicker)
    print(stockData)
    tickerPrice = float(stockData['data'][0]['price'])
    print(f"The price of this ticker is: {tickerPrice}")
    amountSpent = float(stockAmount) * tickerPrice
    # Update Portfolio
    print(f'\nYou have spent {amountSpent} for {stockAmount} shares of {stockTicker}\n')
    Portfolio.portfolios[name]['Overview']['sharesOwned'] += stockAmount
    Portfolio.portfolios[name]['Overview']['netSpent'] += amountSpent
    if stockTicker in Portfolio.portfolios[name]['Stocks']:
        Portfolio.portfolios[name]['Stocks'][stockTicker] += stockAmount
    else:
        Portfolio.portfolios[name]['Stocks'][stockTicker] = stockAmount
    insertPortfolio(name)  # update portfolio in db


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
    retVal = "Your current portfolio information: \n"
    retVal += ('Name: ' + Portfolio.portfolios[name]['Overview']['Name'] + '\n')
    retVal += ('Net Spent: $' + str(Portfolio.portfolios[name]['Overview']['netSpent']) + '\n')
    retVal += ('Net Worth: $' + str(Portfolio.portfolios[name]['Overview']['netWorth']) + '\n')
    retVal += ('Net Gain/Net Loss: $' + str(Portfolio.portfolios[name]['Overview']['netGainLoss']) + '\n')
    retVal += ('Shares Owned: ' + str(Portfolio.portfolios[name]['Overview']['sharesOwned']) + '\n')
    for key, value in Portfolio.portfolios[name]['Stocks'].items():
        retVal += (str(key) + ': ' + str(value) + " shares\n")

    return str(retVal)


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
