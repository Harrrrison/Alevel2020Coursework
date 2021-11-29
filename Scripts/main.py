from PyQt5 import uic, QtWidgets, QtGui, QtSql
from PyQt5.QtWidgets import QApplication, QMainWindow
from Scripts.LogIn import *
import sys
import os
import hashlib
import sqlite3
from sqlCode import *


class SignUpPage(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

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

        # self.logInPage = logInpage()
        # self.stackedWidget.addWidget(self.logInPage)
        # when u have time please read this and do this https://stackoverflow.com/questions/60904814/how-to-change-window-widget-with-pyqt5-using-ui-files

        # getting second password input to verify matching
        self.show()

    def switchwindow(self):
        print("window switch")


        self.cams = logInpage()
        self.cams.show()
        self.close()

    def testCase(self):
        print("test")

    def signupbuttonpressed(self):
        print('password 1: ' + self.password1.text())
        print('password 2: ' + self.password2.text())
        if self.passwordvalidation(
                self.matchingpasswordvalidation()) and self.alreadyausercheck() and self.emailvalidation():
            print("Valid")
            self.passwordhash()
            self.addtodatabase()


    def matchingpasswordvalidation(self):
        if self.password1.text() != self.password2.text():  # making sure the passwords match
            print('non matching passwords please retype')
            self.paswordError_lable.setText('Non-matching passwords')
            return False
        else:
            self.paswordError_label.setText('')
        # showing that the passwords are matching ensuring that neither are stored
            return True  # showing that they arnt matching

    def passwordvalidation(self, matching):  # I could have the mathcing validation outside of the function??
        #
        # this will validate the pass word, i will use subfunctions
        #
        if matching:
            if len(self.password1.text()) < 5 or len(self.password1.text()) > 15:  # password lenght limit of 15 with
                # 5 for security
                self.passwordError_label.setText('Password length error')
                return False
            else:
                return True
        else:
            return False

    def addtodatabase(self):
        #
        # need to inplement the sql code into this fucntion ratehr than just using an array :)
        #
        print(self.userNameInput.text())
        print(self.emailInput.text())
        print(self.password1.text())
        emailInput = self.emailInput.text()
        userNameInput = self.userNameInput.text()
        passwordinput = self.passwordhash()
        execute_query(get_database_connection(),
                      f'INSERT INTO users (email, username, password) VALUES("{emailInput}", "{userNameInput}", "{passwordinput}");')
        self.database.append(self.userNameInput.text())
        self.database.append(self.emailInput.text())
        self.database.append(self.passwordhash())


        print(self.database)


    def termandconditionscheck(self):
        if self.termsOfUse.clicked():
            return True
        else:
            self.termsOfUseMessage.setText('You must agree to the T&C')
            return False

    def emailvalidation(self):
        #
        # the email must contain @ and end in .XYZ
        #

        if "@" not in self.emailInput.text() or "." not in self.emailInput.text():

            print("Email must contain a . and a @")
            self.termsOfUseMessage.setText('Email must contain a . and a @')
            return False
        else:
            email = self.emailInput.text()
            if email == execute_query(get_database_connection(), f"SELECT email FROM users WHERE email = '{email}';"):
                print(type(self.passwordError_label))
                self.termsOfUseMessage.setText('')
                return True
            else:
                self.passwordError_label.setText('This email is already in use')
                return False
    def alreadyausercheck(self):

        try:
            userName = self.userNameInput.text()
            if userName == execute_query(get_database_connection(), f"SELECT username FROM users WHERE username = '{userName}';"):
                print(type(self.passwordError_label))
                self.termsOfUseMessage.setText('username is already in use')

                return False
            else:
                self.termsOfUseMessage.setText('')
                return True

            #
            # Need to check database to see if they are already a user
            #
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
            self.termsOfUseMessage.setText('username is already in use')
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

    def systemValidation(self):
        if self.usernamevalidation() and self.emailvalidation() and self.termandconditionscheck():
            return True
        else:
            return False




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

    window2 = logInpage()

    widget.addWidget(logInWindow)
    # widget.addWidget(mainPage)
