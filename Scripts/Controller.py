from Scripts.LogIn import logInpage
from Scripts.main import *
from Scripts.LogIn import *


class Controller:

    def __init__(self):
        self.loginWindowButton = SignUpPage().signedUpAlready
        self.login = logInpage()
        self.signUp = SignUpPage()
        self.signUp.signedUpAlready.clicked.connect(self.show_login())

    def show_login(self):
        print("working")
        self.login.show()
        self.signUp.close()


    def show_main(self):
        self.window = MainPage()
        self.window.switch_window.connect(self.show_signUpPage())
        self.login.close()
        self.window.show()

    def show_signUpPage(self):
        self.window_two = SignUpPage()
        self.window.close()
        self.window_two.show()
