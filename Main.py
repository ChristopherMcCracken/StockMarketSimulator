from StockMarketApplication.Portfolio import Portfolio
from StockMarketApplication.GrabDataFromAPI import GrabDataFromAPI

# Create new portfolio
p1 = Portfolio({'Overview': {'firstName': 'John', 'lastName': 'Smith', 'netWorth': 0, 'stocksOwned': 0}, 'Stocks': {'': 0}})

# Print out p1 data
print("Your current portfolio information: ")
for key, value in p1.data.items():
    print("" + str(key) + ': ' + str(value))

tickers = []
# Grab desired stock data from user
for i in range(20):  # 20 is the max number of stock queries per API call
    ticker = str(input("\nPlease enter the ticker for a stock you would like to see data for, then hit enter. When you are finished choosing tickers, enter 0: "))
    if ticker == '0':
        print()
        break
    else:
        tickers.append(ticker)

GrabDataFromAPI(tickers)
