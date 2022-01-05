from PyQt6 import QtCore, QtGui, QtWidgets, uic
import sys
import matplotlib

matplotlib.use('Qt5Agg')
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainPage(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    '''
    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi('Front_end_prototype.ui', self)
        self.show()
        self.graphArea1 = self.findChild(QtWidgets.QMdiArea, 'mdiArea')
    '''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainPage()
    app.exec()
