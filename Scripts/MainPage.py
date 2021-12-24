from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import os




class MainPage(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi('Front_end_prototype.ui', self)
        self.show()
        self.graphArea1 = self.findChild(QtWidgets.QMdiArea, 'mdiArea')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainPage()
    app.exec_()
