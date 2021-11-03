from PyQt5 import QtWidgets, QtCore, QtGui

class signUpWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 303, 235))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 2, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.passwordHelpButton = QtWidgets.QToolButton(self.widget)
        self.passwordHelpButton.setObjectName("passwordHelpButton")
        self.gridLayout.addWidget(self.passwordHelpButton, 2, 3, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.name_Lable = QtWidgets.QLabel(self.widget)
        self.name_Lable.setObjectName("name_Lable")
        self.gridLayout.addWidget(self.name_Lable, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.termsOfUse = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.termsOfUse.setFont(font)
        self.termsOfUse.setChecked(False)
        self.termsOfUse.setObjectName("termsOfUse")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.termsOfUse)
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setObjectName("cancelButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cancelButton)
        self.signUpButton = QtWidgets.QPushButton(self.widget)
        self.signUpButton.setObjectName("signUpButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.signUpButton)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.name_Lable.setBuddy(self.name_Lable)

        self.retranslateUi(MainWindow)
        self.cancelButton.clicked.connect(MainWindow.close)
        '''self.termsOfUse.clicked.connect(MainWindow.privacyCheck)
        self.signUpButton.clicked.connect(MainWindow.takeInputs)
        self.lineEdit.editingFinished.connect(MainWindow.takeInputs)
        self.lineEdit_2.editingFinished.connect(MainWindow.takeInputs)
        self.lineEdit_3.editingFinished.connect(MainWindow.takeInputs)
        self.lineEdit_4.editingFinished.connect(MainWindow.takeInputs)'''
        self.signUpButton.clicked.connect(lambda: self.button_clicked())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.passwordHelpButton)
        MainWindow.setTabOrder(self.passwordHelpButton, self.termsOfUse)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Re-type password:"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.passwordHelpButton.setText(_translate("MainWindow", "?"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.name_Lable.setText(_translate("MainWindow", "Name:"))
        self.termsOfUse.setText(_translate("MainWindow", "I agree to the terms of use and privacy policy "))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.signUpButton.setText(_translate("MainWindow", "Sign up"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))

    def test_case(self):
        print("Button click")

    def button_clicked(self):
        user_credentials = []
        user_name = self.lineEdit.text()
        user_email = self.lineEdit_2.text()
        user_password = self.lineEdit_3.text()
        user_password_retype = self.lineEdit_4.text()
        if user_password != user_password_retype:
            print("_Error 1: non matching passwords")
        else:
            print("Strong password!")
        print(user_name)
        user_credentials.append(user_email)
        user_credentials.append(user_name)
        user_credentials.append(user_password)
        print(user_credentials)


if __name__ == "__PlaceholderFile__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signUpWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''things to do in the next stage and get input from users on:
need to hash the password
add further validation
add offline storage 
change password colour when not matching (could add text suggesting that they arnt matching as well?)
anything else...
'''
