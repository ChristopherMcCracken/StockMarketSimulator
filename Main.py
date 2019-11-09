from Portfolio import Portfolio
from GrabDataFromAPI import GrabDataFromAPI


# -------------------------------------------------------------------------------------------------------------------- #
def buySellStocks(portfolioName, stockTicker, stockAmount):
    print(stockTicker)
    stockData = GrabDataFromAPI(stockTicker)
    print(stockData)
    tickerPrice = float(stockData['data'][0]['price'])
    print(f"The price of this ticker is: {tickerPrice}")
    amountSpent = float(stockAmount) * tickerPrice
    # Update Portfolio
    print(f'\nYou have spent {amountSpent} for {stockAmount} shares of {stockTicker}\n')
    Portfolio.portfolios[portfolioName]['Overview']['sharesOwned'] += stockAmount
    Portfolio.portfolios[portfolioName]['Overview']['netWorth'] += amountSpent
    if stockTicker in Portfolio.portfolios[portfolioName]['Stocks']:
        Portfolio.portfolios[portfolioName]['Stocks'][stockTicker] += stockAmount
    else:
        Portfolio.portfolios[portfolioName]['Stocks'][stockTicker] = stockAmount


# -------------------------------------------------------------------------------------------------------------------- #
def getPortfolioInfo(name):
    retVal = "Your current portfolio information: \n"
    for key, value in Portfolio.portfolios[name].items():
        retVal += ("" + str(key) + ': ' + str(value) + "\n")
    return str(retVal)


# -------------------------------------------------------------------------------------------------------------------- #
def createPortfolio(name):
    newPortfolio = Portfolio({'Overview': {'Name': name, 'netWorth': 0, 'sharesOwned': 0}, 'Stocks': {'': 0}})
    return newPortfolio


# -------------------------------------------------------------------------------------------------------------------- #
# Default Portfolio
p1 = Portfolio({'Overview': {'Name': 'Chris', 'netWorth': 0, 'sharesOwned': 0}, 'Stocks': {'': 0}})

# -------------------------------------------------------------------------------------------------------------------- #
