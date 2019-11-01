# -------------------------------------------------------------------------------------------------------------------- #
class Portfolio:
    # Class Variables
    portfolios = {}

    # Constructor
    def __init__(self, data):
        # Instance Variable
        self.data = data
        print(self.data['Overview']['Name'] + ' has been initialized\n')
        self.portfolios[(self.data['Overview']['Name'])] = self.data

    # Class Functions
    def portfolioInfo(self, name):
        retVal = "Your current portfolio information: \n"
        for key, value in self.portfolios[name].data.items():
            retVal += ("" + str(key) + ': ' + str(value) + "\n")
        return retVal
# -------------------------------------------------------------------------------------------------------------------- #
