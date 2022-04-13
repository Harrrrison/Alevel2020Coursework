from PyQt6 import uic, QtWidgets, QtGui, QtSql
from PyQt6.QtWidgets import *

import sqlCode
from Scripts.LogIn import *
import sys
import os
import hashlib
from sqlCode import *
from Scripts.ClearAndRedraw import *


class SignUpPage(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(SignUpPage, self).__init__()
        # uic.loadUi(r'C:\Users\ruthr\PycharmProjects\Alevel2020Coursework\Sign up page.ui', self)
        uic.loadUi(r'/Users/harrisonrigby/PycharmProjects/Alevel2020_Coursework/Sign Up Page.ui', self)
        self.signUpButton = self.findChild(QtWidgets.QPushButton, 'signUpButton')
        self.passwordHelpButton = self.findChild(QtWidgets.QToolButton, 'passwordHelpButton')
        create_database(get_database_connection())

        # Global varibles:
        self.checkBoxState = False
        # Backup database list
        self.database = []

        # Inputs:
        self.userNameInput = self.findChild(QtWidgets.QLineEdit, 'name_lineEdit')
        self.emailInput = self.findChild(QtWidgets.QLineEdit, 'email_LineEdit')
        self.password1 = self.findChild(QtWidgets.QLineEdit, 'password_1')  # getting inital password input
        self.password2 = self.findChild(QtWidgets.QLineEdit, 'password_2')
        # self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.password1.setEchoMode(QtWidgets.QLineEdit)

        # Labels:

        self.passwordError_label = self.findChild(QtWidgets.QLabel, 'passwordError_label')
        self.termsOfUseMessage = self.findChild(QtWidgets.QLabel, 'termsOfUseMessage')
        self.signedUpAlready = self.findChild(QtWidgets.QPushButton, 'hasAccount')

        # Buttons:
        # self.signedUpAlready.clicked.connect(self.testCase)
        # self.signedUpAlready.clicked.connect(self.openMainWindow)
        self.termsOfUse = self.findChild(QtWidgets.QCheckBox, 'termsOfUse')
        self.signedUpAlready.clicked.connect(self.switchwindow)
        self.signUpButton.clicked.connect(self.signupbuttonpressed)
        self.termsOfUse.stateChanged.connect(self.termsnandconditionsToggle)


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
        userName = self.userNameInput.text()
        print(userName)
        if username_validation(get_database_connection(), str(userName)):
            self.termsOfUseMessage.setText('This user name is already in use')
            print("username invalid")
            return False
        else:
            self.termsOfUseMessage.setText(' ')
            print("username valid")
            return True

    def passwordVisibilty(self):
        pass
        # self.password1.setEchoMode(QtWidgets.QLineEdit.password)
        # self.password2.setEchoMode(QtWidgets.QLineEdit.password)

    def signupbuttonpressed(self):
        print('password 1: ' + self.password1.text())
        print('password 2: ' + self.password2.text())
        if (self.passwordvalidation(
                self.matchingpasswordvalidation()) == True) and (
                self.alreadyausercheck() == True) and (
                self.emailvalidation() == True) and (
                self.termsandconditionscheck()):
            print("Valid")
            self.passwordhash()
            self.addtodatabase()

    def matchingpasswordvalidation(self):
        if self.password1.text() != self.password2.text():  # making sure the passwords match
            print('non matching passwords please retype')
            self.termsOfUseMessage.setText('Non-matching passwords')
            return False
        else:
            self.termsOfUseMessage.setText(' ')
            # showing that the passwords are matching ensuring that neither are stored
            return True  # showing that they arnt matching

    def passwordvalidation(self, matching):  # I could have the mathcing validation outside of the function??
        #
        # this will validate the pass word, i will use subfunctions
        #
        if matching:
            if len(self.password1.text()) < 5 or len(self.password1.text()) > 15:  # password lenght limit of 15 with
                # 5 for security
                self.termsOfUseMessage.setText('Password length error')
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
        self.openMainWindow()

    def termsnandconditionsToggle(self):
        if self.checkBoxState == True:
            self.checkBoxState = False
        else:
            self.checkBoxState = True

    def termsandconditionscheck(self):
        if self.checkBoxState == True:
            print("T&C true")
            self.termsOfUseMessage.setText(' ')
            return True
        else:
            print("T&C False")
            self.termsOfUseMessage.setText('The terms and conditions needs to be checked')
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
            if email_validation(get_database_connection(), email):
                self.termsOfUseMessage.setText(' This email is already in use ')
                print('Email invalid')
                return False
            else:
                self.termsOfUseMessage.setText(' ')
                print("Email valid")
                return True

    def alreadyausercheck(self):
        print("already a user check")
        userName = self.userNameInput.text()
        print(userName)
        if username_validation(get_database_connection(), str(userName)):
            self.termsOfUseMessage.setText('This user name is already in use')
            print("username invalid")
            return False
        else:
            self.termsOfUseMessage.setText(' ')
            print("username valid")
            return True

    def passwordhash(self):
        password1 = self.password1.text()
        print("Hashing...")
        return hashlib.sha256(password1.encode('UTF-8')).hexdigest()


    def openMainWindow(self):
        self.cams = MainWindow()
        self.cams.show()
        self.close()


if __name__ == "__main__":
    os.listdir()
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    app = QtWidgets.QApplication(sys.argv)
    window1 = SignUpPage()
    app.exec()
    widget = QtWidgets.QStackedWidget()
    logInWindow = logInpage()
    # mainPage = MainPage()

    window2 = logInpage()

    widget.addWidget(logInWindow)
    # widget.addWidget(mainPage)
