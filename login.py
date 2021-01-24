"""
참고문헌
주식 자동매매 프로그램 (키움api) - 개발환경 구축 https://toptrader.tistory.com/9
OpenAPI+ 로그인하기 https://wikidocs.net/4240
"""

# virtual Environment: py39_32 (python 3.9.1, 32bit environment)

import sys
from PyQt5.QtWidgets import *   # PyQt: python gui package
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    # create window / class MyWindow inherited class QMainWindow
    # properties of QMainWindow were inherited from super().__init__()
    # constructor: CLSID/ProgID

    def __init__(self):
        super().__init__()
        self.setWindowTitle("KiWoom Stock Trading Login")
        self.setGeometry(300, 300, 300, 150)

        # variable kiwoom: Kiwoom Security (QAxWidget inherited QWidget and QAxBase)
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        btnLogin = QPushButton("Login", self)
        btnLogin.move(20, 20)
        btnLogin.clicked.connect(self.btnLoginClicked)
        self.kiwoom.OnEventConnect.connect(self.eventCodeReceived)

        # btnCheckState = QPushButton("Check state", self)
        # btnCheckState.move(20, 60)
        # btnCheckState.clicked.connect(self.btnCheckStateClicked)
        

    def btnLoginClicked(self):
        # call CommConnect() method
        self.kiwoom.dynamicCall("CommConnect()")

    # def btnCheckStateClicked(self):
        # if self.kiwoom.dynamicCall("GetConnectState()") == 0:
        #     self.statusBar().showMessage("Not connected.")
        # else:
        #     self.statusBar().showMessage("Connected.")

    def eventCodeReceived(self, errCode):
        if errCode == 0:
            self.statusBar().showMessage("Login Success!")
        elif errCode == 100:
            self.statusBar().showMessage("User Information Exchange Failed.")
        elif errCode == 101:
            self.statusBar().showMessage("Server Connection Failed.")
        elif errCode == 102:
            self.statusBar().showMessage("Version Process Failed.")
        else:
            self.statusBar().showMessage("Unknown Error.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()