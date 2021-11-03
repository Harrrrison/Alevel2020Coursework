from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from Scripts.main import *



class logInpage(QtWidgets.QMainWindow):

    def __init__(self):
        super(logInpage, self).__init__()
        uic.loadUi('Log-in page.ui', self)
        self.nameInput = self.findChild(QtWidgets.QLineEdit, 'name_LineEdit')
        self.passwordInput = self.findChild(QtWidgets.QLineEdit, 'password_LineEdit')
        self.donthaveaccount = self.findChild(QtWidgets.QPushButton)
        self.donthaveaccount.clicked.connect(self.hide)
        self.donthaveaccount.clicked.connect(SignUpPage.showSelf)



    def showWindowClicked(self):
        print("done")
        logInpage.show(logInpage())





if __name__ == "__LogIn__":
    app = QtWidgets.QApplication(sys.argv)
    window = logInpage()
    app.exec_()


'''TypeError: show(self): first argument of unbound method must have type 'QWidget'''
