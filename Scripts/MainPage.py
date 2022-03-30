from PyQt6 import QtCore, QtGui, QtWidgets, uic
import sys
import matplotlib
# from PyQt6.QtNetwork.QUdpSocket import kwargs

from Data_grabber_functions import *
from datetime import datetime

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
        self.Data_grabber_functions = data_grabbing()
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")

        self.sc = MplCanvas(self, width=5, height=5, dpi=100)
        self.xaxis = []
        self.yaxis = []
        # self.sc.axes.plot([1, 4, 6, 7], [10, 4, 2, 6])
        self.sc.axes.plot([self.current_time], [self.Data_grabber_functions.get_available_memory()])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self._plot_ref = None
        self.update_graph()

        self.show()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start()

    def update_graph(self):
        self.xaxis.append(self.current_time)
        # self.yaxis.append(self.Data_grabber_functions.get_available_memory())

        self.yaxis = self.yaxis[1:] + [self.Data_grabber_functions.get_available_memory()]

        if self._plot_ref is None:

            plot_refs = self.sc.axes.plot(self.xaxis, self.yaxis, 'r')
            self._plot_ref = plot_refs[0]
            xmin, xmax, ymin, ymax = self.sc.axis(**kwargs)
            self.sc.ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

        else:

            self._plot_ref.set_ydata(self.yaxis)

        self.sc.draw()
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
