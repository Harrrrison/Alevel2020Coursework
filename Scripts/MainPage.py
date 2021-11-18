from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from Scripts.main import *

class MainPage(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi('Front_end_prototype.ui', self)
        self.graphArea1 = self.findChild(QtWidgets.QMdiArea, 'mdiArea')