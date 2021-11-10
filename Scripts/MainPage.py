from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from Scripts.main import *

class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(logInpage, self).__init__()
        uic.loadUi('Log-in page.ui', self)