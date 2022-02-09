import sys
import random
import matplotlib
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QHBoxLayout, QComboBox
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

        self.canvas2 = MplCanvas(self, width=5, height=4, dpi=100)

        self.canvas_3 = MplCanvas(self, width=5, height=4, dpi=100)

        # self.ax = plt.axes()

        '''Styling'''
        self.color = 'b'
        # self.ax.set_facecolor("blue")
        # self.setStyleSheet("background-color: rgb(16, 24, 32);")
        # self.ax.title('123')

        layout = QHBoxLayout()

        '''Combo box'''
        self.cb = QComboBox()
        self.cb.addItems(["Blue", "Red", "Green", "Black", "Brown", "Yellow", "White", "Cyan", "Crimson", 'Purple', 'darkviolet'])
        self.cb.currentIndexChanged.connect(self.changecolor)

        toolbar = NavigationToolbar(self.canvas, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.canvas2)
        layout.addWidget(self.canvas_3)
        layout.addWidget(self.cb)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        n_data = 15
        # self.xdata = [0,1,2,3,4,5,6,7,8,9,10,11,12,self.current_time]
        # self.ydata = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.xdata = list(range(n_data))
        self.ydata = [self.Data_grabber_functions.get_percent_memory() for i in range(n_data)]

        self.xdata2 = list(range(n_data))
        self.ydata2 = [self.Data_grabber_functions.get_total_CPU_usage() for i in range(n_data)]

        self.xdata_bytes_sent = list(range(n_data))
        self.ydata_bytes_sent = [self.Data_grabber_functions.get_bytes_sent() for i in range(n_data)]

        self.xdata_bytes_recv = list(range(n_data))
        self.ydata_bytes_recv = [self.Data_grabber_functions.get_bytes_recv() for i in range(n_data)]

        self.xdata_swap_percent = list(range(n_data))
        self.ydata_swap_percent = [self.Data_grabber_functions.get_swap_percent_memory() for i in range(n_data)]

        plt.rc('font', size=10)

        self.update_plot_memory_available()
        self.update_plot_CPU_usage()
        # self.update_plot_swap_percent()
        self.update_plot_bytes_recv()

        self.show()

        # Set up a timer to trigger the graph to be redrawn by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)
        self.timer.timeout.connect(self.update_plot_memory_available)
        self.timer.timeout.connect(self.update_plot_CPU_usage)
        # self.timer.timeout.connect(self.update_plot_swap_percent)
        self.timer.timeout.connect(self.update_plot_bytes_recv)



        # self.timer.timeout.connect(self.update_plot_bytes_sent)

        self.timer.start()

    def update_plot_memory_available(self):

        self.ydata = self.ydata[1:] + [self.Data_grabber_functions.get_percent_memory()]
        self.xdata = self.xdata[1:] + [self.current_time]
        self.canvas.axes.cla()
        self.canvas.axes.plot(self.xdata, self.ydata, self.color, label="memory")

        self.canvas.draw()

    def update_plot_CPU_usage(self):

        self.ydata2 = self.ydata2[1:] + [self.Data_grabber_functions.get_total_CPU_usage()]
        self.xdata2 = self.xdata2[1:] + [self.current_time]
        self.canvas2.axes.cla()
        self.canvas2.axes.plot(self.xdata2, self.ydata2, self.color, label="memory")


        self.canvas2.draw()

    def update_plot_bytes_sent(self):

        self.ydata_bytes_sent = self.ydata_bytes_sent[1:] + [self.Data_grabber_functions.get_bytes_sent()]
        self.xdata_bytes_sent = self.xdata_bytes_sent[1:] + [self.current_time]
        self.canvas_3.axes.cla()
        self.canvas_3.axes.plot(self.xdata_bytes_sent, self.ydata_bytes_sent, self.color, label="memory")

        self.canvas_3.draw()

    def update_plot_bytes_recv(self):
        self.ydata_bytes_recv = self.ydata_bytes_recv[1:] + [self.Data_grabber_functions.get_bytes_recv()]
        self.xdata_bytes_recv = self.xdata_bytes_recv[1:] + [self.current_time]
        self.canvas_3.axes.cla()
        self.canvas_3.axes.plot(self.xdata_bytes_recv, self.ydata_bytes_recv, self.color, label="memory")

        self.canvas_3.draw()

    def update_plot_swap_percent(self):

        self.ydata_swap_percent = self.ydata_swap_percent[1:] + [self.Data_grabber_functions.get_swap_percent_memory()]
        self.xdata_swap_percent = self.xdata_swap_percent[1:] + [self.current_time]
        self.canvas_3.axes.cla()
        self.canvas_3.axes.plot(self.xdata_swap_percent, self.ydata_swap_percent, self.color, label="memory")

        self.canvas_3.draw()

    def changecolor(self):
        self.color = self.cb.currentText()

    def update_time(self):
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()
