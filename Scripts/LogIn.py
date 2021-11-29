from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import sqlite3
from sqlCode import *
import hashlib
from Scripts.MainPage import *





class logInpage(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()


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
        self.donthaveaccount.clicked.connect(self.showWindowClicked)

        # Classes:
        mainWindow = MainPage()



    def showWindowClicked(self):
        #
        # On button click it should switch window
        #
        print("show")

    def validateUser(self):
        #
        # needs to have database password validation
        #
        if self.getUserInput():
            if self.checkPassword():
                self.mainWindow.show()
                self.close()


        else:
            self.errorLabel.setText("Incorrect password for this account")


    def getUserInput(self):
        try:
            userName = self.nameInput.text()
            if userName == execute_query(get_database_connection(), f"SELECT username FROM users WHERE username = '{userName}';"):
                print(type(self.passwordError_label))

                return False
            else:

                return True
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
            return False

    def checkPassword(self):
        try:
            password = self.paasswordHash()
            if password == execute_query(get_database_connection(),
                                         f"SELECT password FROM users WHERE password = '{password}';"):
                print(type(self.passwordError_label))

                return False
            else:

                return True
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
            return False

    def paasswordHash(self):
        password1 = self.passwordInput.text()
        print("Hashing...")
        return hashlib.sha256(password1.encode('UTF-8')).hexdigest()






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = logInpage()
    app.exec_()

'''TypeError: show(self): first argument of unbound method must have type 'QWidget'''
