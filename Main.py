from Portfolio import Portfolio
from GrabDataFromAPI import GrabDataFromAPI


# -------------------------------------------------------------------------------------------------------------------- #
def buySellStocks(portfolioName):
    tickersToGrab = promptForTickers()
    stockData = GrabDataFromAPI(tickersToGrab)
    ticker = str(input("Please enter the ticker for a stock you would like to purchase/sell: "))
    tickerPrice = float(stockData['data'][tickersToGrab[ticker]]['price'])
    purchaseCount = int(input(f'\nThe price of this ticker is: {tickerPrice}, how many would you like to buy/sell? (negative number to sell): '))
    amountSpent = float(purchaseCount) * tickerPrice
    # Update Portfolio
    print(f'\nYou have spent {amountSpent} for {purchaseCount} shares of {ticker}\n')
    Portfolio.portfolios[portfolioName]['Overview']['sharesOwned'] += purchaseCount
    Portfolio.portfolios[portfolioName]['Overview']['netWorth'] += amountSpent
    if ticker in Portfolio.portfolios[portfolioName]['Stocks']:
        Portfolio.portfolios[portfolioName]['Stocks'][ticker] += purchaseCount
    else:
        Portfolio.portfolios[portfolioName]['Stocks'][ticker] = purchaseCount


# -------------------------------------------------------------------------------------------------------------------- #
def promptForTickers():
    tickers = {}
    for i in range(20):  # 20 is the max number of stock queries per API call
        ticker = str(input("\nPlease enter the ticker for a stock you would like to see data for, then hit enter. When you are finished choosing tickers, enter nothing: "))
        if ticker in tickers:
            print("Duplicate Ticker, try again.")
            i -= i  # dont want to increment i in this instance
            continue
        elif ticker == '':
            print()
            break
        else:
            tickers[ticker] = i
    print(tickers)
    print()
    return tickers


# -------------------------------------------------------------------------------------------------------------------- #
def getPortfolioInfo(name):
    return str(Portfolio.portfolios[name])


# -------------------------------------------------------------------------------------------------------------------- #
def createPortfolio(name):
    newPortfolio = Portfolio({'Overview': {'Name': name, 'netWorth': 0, 'sharesOwned': 0}, 'Stocks': {'': 0}})
    getPortfolioInfo(name)
    return newPortfolio


# -------------------------------------------------------------------------------------------------------------------- #
# Default Portfolio
p1 = Portfolio({'Overview': {'Name': 'John', 'netWorth': 0, 'sharesOwned': 0}, 'Stocks': {'': 0}})

# -------------------------------------------------------------------------------------------------------------------- #
