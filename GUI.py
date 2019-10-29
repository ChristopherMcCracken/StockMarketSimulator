from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette, QColor

from StockMarketApplication import Main


class Ui_StockMarketApplication(object):
    def setupUi(self, StockMarketApplication):
        StockMarketApplication.setObjectName("StockMarketApplication")
        StockMarketApplication.resize(460, 330)
        self.gridLayout = QtWidgets.QGridLayout(StockMarketApplication)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(StockMarketApplication)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.retranslateUi(StockMarketApplication)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("pressed()"), Main.main)  # when button is pressed main is ran
        QtCore.QMetaObject.connectSlotsByName(StockMarketApplication)

    def retranslateUi(self, StockMarketApplication):
        StockMarketApplication.setWindowTitle(QtWidgets.QApplication.translate("StockMarketApplication", "StockMarketApplication", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("StockMarketApplication", "Run Program", None, -1))


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
    StockMarketApplication = QtWidgets.QWidget()
    ui = Ui_StockMarketApplication()
    ui.setupUi(StockMarketApplication)
    StockMarketApplication.show()
    sys.exit(app.exec_())
