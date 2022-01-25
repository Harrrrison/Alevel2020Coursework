import sys
import random
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import ylim

matplotlib.use('Qt5Agg')

from PyQt6 import QtCore, QtWidgets

from Data_grabber_functions import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)




class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.Data_grabber_functions = data_grabbing()

        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)


        toolbar = NavigationToolbar(self.canvas, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        n_data = 15
        # self.xdata = [0,1,2,3,4,5,6,7,8,9,10,11,12,self.current_time]
        # self.ydata = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.xdata = list(range(n_data))
        self.ydata = [self.Data_grabber_functions.get_available_memory() for i in range(n_data)]

        plt.rc('font', size=10)

        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [self.Data_grabber_functions.get_available_memory()]
        self.xdata = self.xdata[1:] + [self.current_time]
        self.canvas.axes.cla()
        self.canvas.axes.plot(self.xdata, self.ydata, 'b', label="memory")
        # Trigger the canvas to update and redraw.

        self.canvas.draw()

    def update_time(self):
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()