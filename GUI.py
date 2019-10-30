from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette, QColor
from PySide2.QtWidgets import QMainWindow, QApplication

from StockMarketApplication import Main


# -------------------------------------------------------------------------------------------------------------------- #
class Ui_Application(object):
# -------------------------------------------------------------------------------------------------------------------- #
    def viewPortfolio(self):
        self.viewPortfolioWindow = QMainWindow()
        self.viewPortfolioWindow.resize(500, 500)
        self.viewPortfolioWindow.setWindowTitle("Current Tab")
        label = QtWidgets.QLabel(self.viewPortfolioWindow)
        label.move(50, 50)
        label.setText(Main.getPortfolioInfo())
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
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), Main.buySellStocks)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.viewPortfolio)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), Main.createPortfolio)
        QtCore.QMetaObject.connectSlotsByName(Application)

# -------------------------------------------------------------------------------------------------------------------- #
    def retranslateUi(self, Application):
        Application.setWindowTitle(
            QtWidgets.QApplication.translate("Application", "Stock Market Application", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Application", "Create Portfolio", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Application", "Buy/Sell Stocks", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Application", "View Portfolio", None, -1))


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    import sys

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
