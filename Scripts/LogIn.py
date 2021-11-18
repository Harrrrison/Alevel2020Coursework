from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from Scripts.main import *



class logInpage(QtWidgets.QMainWindow):

    def __init__(self):
        super(logInpage, self).__init__()
        uic.loadUi('Log-in page.ui', self)

        # Input boxes:
        self.nameInput = self.findChild(QtWidgets.QLineEdit, 'name_LineEdit')
        self.passwordInput = self.findChild(QtWidgets.QLineEdit, 'password_LineEdit')

        # Labels:
        self.errorLabel = self.findChild(QtWidgets.QLabel, 'errorLabel')
        self.passwordLabel = self.findChild(QtWidgets.QLabel, 'passwordLabel')

        # Buttons:
        self.logInButton = self.findChild(QtWidgets.QPushButton, 'logInButton')
        self.logInButton.clicked.connect(self.validateUser)
        self.donthaveaccount = self.findChild(QtWidgets.QPushButton)
        self.donthaveaccount.clicked.connect(self.hide)
        self.donthaveaccount.clicked.connect(SignUpPage.showSelf)

        # Classes:



    def showWindowClicked(self):
        #
        # On button click it should switch window
        #
        print("done")
        logInpage.show(logInpage())

    def validateUser(self):
        #
        # needs to have database password validation
        #
        if self.passwordInput == "123456789":
            print("valid")
            self.hide()

        else:
            self.errorLabel.setText("Incorrect password for this account")







if __name__ == "__LogIn__":
    app = QtWidgets.QApplication(sys.argv)
    window = logInpage()
    app.exec_()


'''TypeError: show(self): first argument of unbound method must have type 'QWidget'''
