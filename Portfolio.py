# -------------------------------------------------------------------------------------------------------------------- #
class Portfolio:
    # Class Variables

    # Constructor
    def __init__(self, data):
        # Instance Variable
        self.data = data

    # Class Functions
    def portfolioInfo(self):
        retVal = "Your current portfolio information: \n"
        for key, value in self.data.items():
            retVal += ("" + str(key) + ': ' + str(value) + "\n")
        return retVal
# -------------------------------------------------------------------------------------------------------------------- #
