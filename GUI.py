from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QPalette, QColor, Qt, QFont
from PySide2.QtWidgets import QMainWindow, QInputDialog, QWidget, QPushButton, QFormLayout, QLineEdit, QLabel
import Main
from Main import createPortfolio
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
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
            label.setStyleSheet("QLabel {font: 20pt Calibri}")
            label.adjustSize()
            self.viewPortfolioWindow.show()

    # ---------------------------------------------------------------------------------------------------------------- #
    def plotStockHistory(self):
        self.inputWindow = inputDialog()
        ticker = self.inputWindow.gettext("Enter stock to view: ")
        if ticker is not None:
            daysBack = self.inputWindow.getint("Enter number of days to view: ")
            if daysBack is not None:
                self.wid = QtWidgets.QWidget()
                self.wid.setWindowTitle(f"{ticker} Stock History")
                self.wid.resize(1000, 500)
                grid = QtWidgets.QGridLayout(self.wid)

                fig = Figure()
                axs = fig.add_subplot(111)

                data = GrabDataFromAPI.grabStockHistory(ticker, daysBack)
                days = list(range(0, daysBack))
                axs.set_xlabel('Days Ago')
                axs.set_ylabel('Price in US Dollars')
                axs.set_title(ticker + ' Closing Price History')
                axs.grid(True)
                fig.patch.set_facecolor('silver')
                axs.set_facecolor('grey')
                axs.plot(days, data, color='cyan')

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
        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 1)

        self.retranslateUi(Application)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.buySellStocks)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.viewPortfolioWindow)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.createPortfolioWindow)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.plotStockHistory)
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
        items = ("P1", "P2", "P3", "P4")

        item, ok = QInputDialog.getItem(self, prompt,
                                        "List of Portfolios", items, 0, False)

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
