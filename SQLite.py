import sqlite3
from Portfolio import Portfolio


# -------------------------------------------------------------------------------------------------------------------- #
def insertPortfolio(name):
    with conn:
        c.execute('INSERT OR REPLACE INTO overview VALUES (:Name, :sharesOwned, :netWorth, :netSpent, :netGainLoss)',
                  {'Name': Portfolio.portfolios[name]['Overview']['Name'],
                   'sharesOwned': Portfolio.portfolios[name]['Overview']['sharesOwned'],
                   'netWorth': Portfolio.portfolios[name]['Overview']['netWorth'],
                   'netSpent': Portfolio.portfolios[name]['Overview']['netSpent'],
                   'netGainLoss': Portfolio.portfolios[name]['Overview']['netGainLoss']})
        for stockName, stockValue in Portfolio.portfolios[name]['Stocks'].items():
            c.execute('INSERT OR REPLACE INTO stocks VALUES (:Name, :Stock, :count)',
                      {'Name': Portfolio.portfolios[name]['Overview']['Name'],
                       'Stock': stockName,
                       'count': stockValue})


# -------------------------------------------------------------------------------------------------------------------- #
def loadPortfolioFromDB(name):
    p = {'Overview': {'Name': '', 'sharesOwned': 0, 'netWorth': 0, 'netSpent': 0, 'netGainLoss': 0},
         'Stocks': {}}

    c.execute("SELECT * FROM overview WHERE Name=:Name", {'Name': name})
    fetchedOverviewValues = c.fetchall()
    for index, key in enumerate(p['Overview']):
        p['Overview'][key] = fetchedOverviewValues[0][index]

    c.execute("SELECT * FROM stocks WHERE Name=:Name", {'Name': name})
    fetchedStockValues = c.fetchall()
    for index, key in enumerate(fetchedStockValues):
        p['Stocks'][fetchedStockValues[index][1]] = fetchedStockValues[index][2]

    print(p)
    Portfolio(p)



# -------------------------------------------------------------------------------------------------------------------- #
conn = sqlite3.connect('Portfolio.db')
c = conn.cursor()

c.execute("""CREATE TABLE if not exists overview(
             Name text,
             sharesOwned integer,
             netWorth real,
             netSpent real,
             netGainLoss real,
             UNIQUE(Name)
          )""")

c.execute("""CREATE TABLE if not exists stocks(
             Name text,
             Stock text,
             count integer
          )""")
