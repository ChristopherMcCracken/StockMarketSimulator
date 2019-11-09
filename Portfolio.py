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
# -------------------------------------------------------------------------------------------------------------------- #
