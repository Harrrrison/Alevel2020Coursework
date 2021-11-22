from PyQt5 import uic, QtWidgets, QtGui, QtSql
from PyQt5.QtWidgets import QApplication, QMainWindow
from Scripts.LogIn import *
from Scripts.MainPage import *
import sys
import os
import hashlib
import sqlite3
from sqlCode import *



class SignUpPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignUpPage, self).__init__()
        uic.loadUi('Sign up page.ui', self)
        self.signUpButton = self.findChild(QtWidgets.QPushButton, 'signUpButton')
        create_database(get_database_connection())
        # Inputs:
        self.userNameInput = self.findChild(QtWidgets.QLineEdit, 'name_lineEdit')
        self.emailInput = self.findChild(QtWidgets.QLineEdit, 'email_LineEdit')
        self.password1 = self.findChild(QtWidgets.QLineEdit, 'password_1')  # getting inital password input
        self.password2 = self.findChild(QtWidgets.QLineEdit, 'password_2')
        self.database = []

        # Labels:
        self.termsOfUse = self.findChild(QtWidgets.QCheckBox, 'termsOfUse')
        self.passwordError_label = self.findChild(QtWidgets.QLabel, 'passwordError_label')
        self.termsOfUseMessage = self.findChild(QtWidgets.QLabel, 'termsOfUseMessage')
        self.signedUpAlready = self.findChild(QtWidgets.QPushButton, 'hasAccount')

        # Buttons:
        self.signedUpAlready.clicked.connect(self.switchwindow)
        self.signUpButton.clicked.connect(self.signupbuttonpressed)
        self.signedUpAlready.clicked.connect(self.testCase)

        self.logInPage = logInpage()
        # self.stackedWidget.addWidget(self.logInPage)
        # when u have time please read this and do this https://stackoverflow.com/questions/60904814/how-to-change-window-widget-with-pyqt5-using-ui-files


        # getting second password input to verify matching
        self.show()

    def switchwindow(self):
        print("window switch")
        nextWindow = logInpage()
        nextWindow.show()
        self.close()


    def testCase(self):
        print("test")

    def signupbuttonpressed(self):
        print('password 1: ' + self.password1.text())
        print('password 2: ' + self.password2.text())
        if self.passwordvalidation(
                self.matchingpasswordvalidation()) and self.termandconditionscheck() and self.emaivalidation():
            self.passwordhash(self.password1)
            self.addtodatabase()

    def matchingpasswordvalidation(self):
        if self.password1.text() != self.password2.text():  # making sure the passwords match
            print('non matching passwords please retype')
            self.paswordError_lable.setText('Non-matching passwords')
            return False  # showing that the passwords are matching ensuring that neither are stored
        return True  # showing that they arnt matching

    def passwordvalidation(self, matching):  # I could have the mathcing validation outside of the function??
        #
        # this will validate the pass word, i will use subfunctions
        #
        if matching:
            if len(self.password1.text()) < 5 or len(self.password1.text()) > 15:  # password lenght limit of 15 with
                # 5 for security
                self.paswordError_lable.setText('Password length error')
            else:
                self.addtodatabase()
        else:
            return False

    def addtodatabase(self):
        #
        # need to inplement the sql code into this fucntion ratehr than just using an array :)
        #
        print(self.userNameInput.text())
        print(self.emailInput.text())
        print(self.password1.text())
        execute_query(get_database_connection(), "INSERT INTO users (email, username, password) VALUES (self.emailInput, self.userNameInput, self.passwordhash());")
        self.database.append(self.userNameInput.text())
        self.database.append(self.emailInput.text())
        self.database.append(self.passwordhash())

        print(self.database)

    def termandconditionscheck(self):
        if self.termsOfUse:
            return True
        else:
            self.termsOfUseMessage.setText('You must agree to the T&C')
            return False

    def emaivalidation(self):
        #
        # the email must contain @ and end in .XYZ
        #
        if not (self.alreadyausercheck()):
            print("hi")
            #
            # Email validation here please
            #
        else:
            self.passwordError_label.setText('There is already a user with this email')

    def alreadyausercheck(self):
        if execute_query(get_database_connection(), "SELECT user FROM users WHERE user=self.userNameInput;"):
            #
            # Need to check database to see if they are already a user
            #
            return True
        else:
            return False

    def passwordhash(self):
        #
        # I will use a real hashing algorythm and store the it next to the username and email
        # This will be then used to retreve user log in details
        #
        password1 = self.password1.text()
        print("Hashing...")
        return hashlib.sha256(password1.encode('UTF-8')).hexdigest()


    def usernamevalidation(self):
        if not (self.usernamenotinsystem()):
            #
            # continue the validation of the user name, char lenght data type etc.
            #
            return True
        else:
            self.passwordError_label.setText('That username is already in use try anther one')

    def usernamenotinsystem(self):
        if execute_query(get_database_connection(), "SELECT user FROM users WHERE user=self.userNameInput;"):
            return False
        else:
            return True






if __name__ == "__main__":
    os.listdir()
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    app = QtWidgets.QApplication(sys.argv)
    window1 = SignUpPage()
    app.exec_()
    widget = QtWidgets.QStackedWidget()
    logInWindow = logInpage()
    # mainPage = MainPage()

    window2 = SignUpPage()

    widget.addWidget(logInWindow)
    # widget.addWidget(mainPage)
