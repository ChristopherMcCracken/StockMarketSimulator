from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QPalette, QColor, Qt
from PySide2.QtWidgets import QMainWindow, QInputDialog, QWidget, QPushButton, QFormLayout, QLineEdit, QScrollArea
import Main
from Main import createPortfolio
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import GrabDataFromAPI
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates, ticker
import matplotlib as mpl
from mpl_finance import candlestick_ohlc
import GrabDataFromAPI

# -------------------------------------------------------------------------------------------------------------------- #
class Ui_Application(object):
    # ---------------------------------------------------------------------------------------------------------------- #
    def buySellStocks(self):
        self.inputWindow = inputDialog()
        portfolioName = self.inputWindow.gettext("Enter portfolio to update: ")
        if portfolioName is not None:
            stockTicker = self.inputWindow.gettext("Enter the stock name to trade: ")
            if stockTicker is not None:
                tickerPrice = Main.getStockPrice(portfolioName, stockTicker)
                stockAmount = self.inputWindow.getint(
                    f"The price of this stock is: ${tickerPrice}\nEnter how many shares to buy/sell: ")
                if stockAmount is not None:
                    Main.buySellStocks(portfolioName, stockTicker, stockAmount, tickerPrice)

    # ---------------------------------------------------------------------------------------------------------------- #
    def createPortfolioWindow(self):
        self.inputWindow = inputDialog()
        portfolioName = self.inputWindow.gettext()
        if portfolioName is not None:
            createPortfolio(portfolioName)
            return portfolioName

    # ---------------------------------------------------------------------------------------------------------------- #
    def viewPortfolioWindow(self):
        self.inputWindow = inputDialog()
        portfolioName = self.inputWindow.gettext()
        if portfolioName is not None:
            self.viewPortfolioWindow = QMainWindow()
            self.viewPortfolioWindow.resize(1000, 500)
            self.viewPortfolioWindow.setWindowTitle("View Portfolio")
            label = QtWidgets.QLabel(self.viewPortfolioWindow)
            label.move(50, 50)
            label.setText(Main.getPortfolioInfo(portfolioName))
            label.setStyleSheet("QLabel {font: 22pt Courier}")
            label.adjustSize()
            self.viewPortfolioWindow.show()

    # ---------------------------------------------------------------------------------------------------------------- #
    def detailedStockInfo(self):
        self.inputWindow = inputDialog()
        stockTickers = self.inputWindow.gettext("Enter stock name: ")
        if stockTickers is not None:
            self.detailedStockInfo = QMainWindow()
            self.detailedStockInfo.resize(1000, 1000)
            self.detailedStockInfo.setWindowTitle("Detailed Stock Info")
            label = QtWidgets.QLabel(self.detailedStockInfo)
            label.move(50, 50)
            label.setText(Main.getAllStockData(stockTickers))
            label.setStyleSheet("QLabel {font: 22pt Courier}")
            label.adjustSize()
            self.detailedStockInfo.show()

    # ---------------------------------------------------------------------------------------------------------------- #
    def plotStockHistory(self):
        self.inputWindow = inputDialog()
        tickerChoice = self.inputWindow.gettext("Enter stock to view: ")
        if tickerChoice is not None:
            numberOfDays = self.inputWindow.getint("Enter number of days to view: ")
            if numberOfDays is not None:
                chartChoice = self.inputWindow.getItem("Choose chart type: ")
                print(chartChoice)
                self.wid = QtWidgets.QWidget()
                self.wid.setWindowTitle(f"{tickerChoice} Stock History")
                self.wid.resize(1000, 500)
                grid = QtWidgets.QGridLayout(self.wid)
                fig, ax = plt.subplots()
                data = GrabDataFromAPI.grabStockHistory(tickerChoice, numberOfDays)
                fig.patch.set_facecolor('silver')
                ax.set_facecolor('grey')
                if chartChoice != 'Candlestick':
                    x = [dates.datestr2num(data[i][0]) for i in range(numberOfDays)]
                    y = [float(data[i][4]) for i in range(numberOfDays)]
                    ax.xaxis.set_major_formatter(dates.DateFormatter('%m/%d/%Y'))
                    ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
                    ax.set_xlabel('Date')
                    ax.set_ylabel('Price in USD')
                    ax.set_title(tickerChoice + ' Closing Price History')
                    ax.grid(True)
                    ax.plot(x, y, color='cyan')
                else:
                    ohlc_data = []  # Open High Low Close Data
                    for row in data:
                        ohlc_data.append((dates.datestr2num(row[0]), np.float64(row[1]), np.float64(row[2]),
                                          np.float64(row[3]), np.float64(row[4])))

                    candlestick_ohlc(ax, ohlc_data, width=float(0.5), colorup='cyan', colordown='orange', alpha=0.8)
                    ax.xaxis.set_major_formatter(dates.DateFormatter('%m/%d/%Y'))
                    ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
                    plt.xticks(rotation=30)
                    plt.grid()
                    plt.xlabel('Date')
                    plt.ylabel('Price in USD')
                    plt.title(tickerChoice + ' Candlestick Chart')
                    plt.tight_layout()
                canvas = FigureCanvas(fig)
                grid.addWidget(canvas, 0, 0)
                self.wid.show()

    # ------------------------------------------------------------------------------------------------------------ #
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(1000, 1000)

        self.gridLayout = QtWidgets.QGridLayout(Application)
        self.gridLayout.setObjectName("gridLayout")

        # Top Label
        self.label = QtWidgets.QLabel(Application)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel {font: 30pt Elephant; color: #e8fcca}")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        # First Button
        self.pushButton = QtWidgets.QPushButton(Application)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('QPushButton {font: 25pt Elephant}')
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        # Second Button
        self.pushButton_2 = QtWidgets.QPushButton(Application)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('QPushButton {font: 25pt Elephant}')
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)

        # Third Button
        self.pushButton_3 = QtWidgets.QPushButton(Application)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet('QPushButton {font: 25pt Elephant}')
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)

        # Fourth Button
        self.pushButton_4 = QtWidgets.QPushButton(Application)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet('QPushButton {font: 25pt Elephant}')
        self.gridLayout.addWidget(self.pushButton_4, 5, 0, 1, 1)

        # Fifth Button
        self.pushButton_5 = QtWidgets.QPushButton(Application)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet('QPushButton {font: 25pt Elephant}')
        self.gridLayout.addWidget(self.pushButton_5, 6, 0, 1, 1)

        # Lines
        self.line = QtWidgets.QFrame(Application)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.line_2 = QtWidgets.QFrame(Application)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line")
        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 1)

        self.retranslateUi(Application)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.buySellStocks)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.viewPortfolioWindow)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.createPortfolioWindow)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.plotStockHistory)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), self.detailedStockInfo)

        QtCore.QMetaObject.connectSlotsByName(Application)

    # ------------------------------------------------------------------------------------------------------------ #
    def retranslateUi(self, Application):
        Application.setWindowTitle(QtWidgets.QApplication.translate("Application", "Virtual Stock Market Application", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Application", "Buy/Sell Stocks", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Application", "Create Portfolio", None, -1))
        self.label.setText(
            QtWidgets.QApplication.translate("Application", "Virtual Stock Market Application", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Application", "Plot Stock History", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Application", "View Portfolio", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("Application", "View Detailed Stock Data", None, -1))


# -------------------------------------------------------------------------------------------------------------------- #
class inputDialog(QWidget):
    def __init__(self, parent=None):
        super(inputDialog, self).__init__(parent)

        infoList = ['', '', '']

        layout = QFormLayout()
        self.btn = QPushButton("Choose from list")
        self.btn.clicked.connect(self.getItem)

        self.le = QLineEdit()
        layout.addRow(self.btn, self.le)
        self.btn1 = QPushButton("get name")
        self.btn1.clicked.connect(self.gettext)

        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)
        self.btn2 = QPushButton("Enter an integer")
        self.btn2.clicked.connect(self.getint)

        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)
        self.setLayout(layout)
        self.setWindowTitle("Input Dialog demo")

    # ---------------------------------------------------------------------------------------------------------------- #
    def getItem(self, prompt="Enter an option: "):
        items = ('Candlestick', 'Closing Prices')

        item, ok = QInputDialog.getItem(self, prompt,
                                        'Choose a chart type:', items, 0, False)

        if ok and item:
            self.le.setText(item)
            return str(item)
        else:
            return None

    # ---------------------------------------------------------------------------------------------------------------- #
    def gettext(self, prompt="Enter The Portfolio Name: "):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', prompt)

        if ok:
            self.le1.setText(str(text))
            return str(text)
        else:
            return None

    # ---------------------------------------------------------------------------------------------------------------- #
    def getint(self, prompt="Enter a number: "):
        num, ok = QInputDialog.getInt(self, "integer input dialog", prompt)

        if ok:
            self.le2.setText(str(num))
            return int(num)
        else:
            return None


# -------------------------------------------------------------------------------------------------------------------- #
def main():
    app = QtWidgets.QApplication(sys.argv)

    # Change palette to allow for for dark theme
    app.setStyle('Windows')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(82, 81, 81))  # HEX 525151
    palette.setColor(QPalette.Button, QColor(82, 81, 81))  # HEX 525151
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    Application = QtWidgets.QWidget()
    ui = Ui_Application()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())


# -------------------------------------------------------------------------------------------------------------------- #
main()
