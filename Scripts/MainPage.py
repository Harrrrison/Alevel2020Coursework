from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys


class MainPage(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainPage, self).__init__()
        self.show()
        self.graphArea1 = self.findChild(QtWidgets.QMdiArea, 'mdiArea')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainPage()
    app.exec_()
