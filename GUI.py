import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPalette, QColor, Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QInputDialog, QWidget, QPushButton, QLabel, QFormLayout, QLineEdit
import Main
from Main import createPortfolio


# -------------------------------------------------------------------------------------------------------------------- #
class Ui_Application(object):
    # -------------------------------------------------------------------------------------------------------------------- #
    def buySellStocks(self):
        self.createPortfolioWindow = inputDialog()
        portfolioName = self.createPortfolioWindow.gettext()
        Main.buySellStocks(portfolioName)

    def createPortfolioWindow(self):
        self.createPortfolioWindow = inputDialog()
        portfolioName = self.createPortfolioWindow.gettext()
        print(f'Portfolio Name: {portfolioName}\n')
        createPortfolio(portfolioName)
        return portfolioName

    def viewPortfolioWindow(self):
        self.createPortfolioWindow = inputDialog()
        portfolioName = self.createPortfolioWindow.gettext()
        self.viewPortfolioWindow = QMainWindow()
        self.viewPortfolioWindow.resize(500, 500)
        self.viewPortfolioWindow.setWindowTitle("viewPortfolio")
        label = QtWidgets.QLabel(self.viewPortfolioWindow)
        label.move(50, 50)
        label.setText(Main.getPortfolioInfo(portfolioName))
        label.adjustSize()
        self.viewPortfolioWindow.show()

    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(500, 500)  # Default size
        self.gridLayout = QtWidgets.QGridLayout(Application)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(Application)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Application)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Application)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.retranslateUi(Application)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.buySellStocks)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.viewPortfolioWindow)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.createPortfolioWindow)
        QtCore.QMetaObject.connectSlotsByName(Application)

    # -------------------------------------------------------------------------------------------------------------------- #
    def retranslateUi(self, Application):
        Application.setWindowTitle(
            QtWidgets.QApplication.translate("Application", "Stock Market Application", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Application", "Create Portfolio", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Application", "Buy/Sell Stocks", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Application", "View Portfolio", None, -1))


# -------------------------------------------------------------------------------------------------------------------- #
class inputDialog(QWidget):
    # -------------------------------------------------------------------------------------------------------------------- #
    def __init__(self, parent=None):
        super(inputDialog, self).__init__(parent)  # call initializer

        layout = QFormLayout()

        # Add button to row
        self.row1 = QLineEdit()
        self.btn1 = QPushButton("Name: ")
        self.btn1.clicked.connect(self.gettext)

    # -------------------------------------------------------------------------------------------------------------------- #
    def gettext(self):
        text = QInputDialog.getText(self, 'Create Portfolio', 'Enter your name:')
        self.row1.setText(str(text))
        return text[0]  # text[1] holds true


# -------------------------------------------------------------------------------------------------------------------- #
def main():
    app = QtWidgets.QApplication(sys.argv)

    # Change palette to allow for for dark theme
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
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
