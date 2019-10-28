# -------------------------------------------------------------------------------------------------------------------- #
class Portfolio:
    # Class Variables

    # Constructor
    def __init__(self, data):
        # Instance Variable
        self.data = data

    # Class Functions
    def printPortfolioInfo(self):
        print("Your current portfolio information: ")
        for key, value in self.data.items():
            print("" + str(key) + ': ' + str(value))
# -------------------------------------------------------------------------------------------------------------------- #
