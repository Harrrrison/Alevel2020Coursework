import sys
import random
import matplotlib
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QHBoxLayout, QComboBox, QTableWidgetItem, QTableWidget, QVBoxLayout, QWidget
from matplotlib.pyplot import ylim

matplotlib.use('Qt5Agg')

from PyQt6 import QtCore, QtWidgets

from Data_grabber_functions import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure


class partsTable(QWidget):
    def __init__(self):
        super().__init__()
        self.Data_grabber_functions = data_grabbing()

        self.createTable()

    def createTable(self):
        vbox = QVBoxLayout()

        # add table
        table = QTableWidget(self)
        table.setColumnCount(6)
        table.setRowCount(1)

        table.setHorizontalHeaderLabels(['System', 'Node Name', 'Release', 'Version', 'Machine', 'Processor'])
        table_values = []

        # Raw system info array
        data = [self.Data_grabber_functions.get_system_name(), self.Data_grabber_functions.get_system_node(),
                self.Data_grabber_functions.get_system_release(),
                self.Data_grabber_functions.get_system_version(),
                self.Data_grabber_functions.get_system_machine(),
                self.Data_grabber_functions.get_system_processor()]

        table_values.append(data)  # the data from the list need to be appended into the table values

        row = 0
        for i in table_values:  # a loop is needed to put them in the correct collums
            col = 0
            for item in i:  # Will itterate through all the items that have been added to the item list
                # then append them to the collum
                table.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row += 1

        for i in range(5):
            table.resizeColumnToContents(i)

        vbox.addWidget(table)
        self.setLayout(vbox)
        self.show()


class MplCanvas(FigureCanvas):

    # In this class the canvas is created -- this will give the graph a place to sit
    # The width height and dpi can all be adjusted with an integer value

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.table_of_system_info = partsTable()
        self.Data_grabber_functions = data_grabbing()

        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")

        # instantiating the canvas'
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.set_ylabel("% RAM used")
        self.setCentralWidget(self.canvas)

        self.canvas2 = MplCanvas(self, width=5, height=4, dpi=100)

        self.canvas_3 = MplCanvas(self, width=5, height=4, dpi=100)

        self.canvas_3_type = ""
        self.time_interval = 1000


        '''Styling'''
        self.color = 'b'

        layout = QHBoxLayout()

        '''Combo box to change color'''
        self.cb = QComboBox()
        self.cb.addItems(
            ["Blue", "Red", "Green", "Black", "Brown", "Yellow", "White", "Cyan", "Crimson", 'Purple', 'darkviolet'])
        self.cb.currentIndexChanged.connect(self.changecolor)

        '''Third graph combo box'''
        self.cb2 = QComboBox()
        self.cb2.addItems(
            ["Bytes received", "Bytes sent", "Swap %"])
        self.cb2.currentIndexChanged.connect(self.change_graph)

        '''Graph update combo box'''
        self.cb3 = QComboBox()
        self.cb3.addItems(
            ["1000", "500", "2500", "5000", "10000", "60000"])
        self.cb3.currentIndexChanged.connect(self.update_time_interval)

        toolbar = NavigationToolbar(self.canvas, self)
        toolbar2 = NavigationToolbar(self.canvas2, self)
        toolbar3 = NavigationToolbar(self.canvas_3, self)

        # Layout of the while widget page using grid layout
        layout = QtWidgets.QGridLayout()
        layout.addWidget(toolbar, 0, 0, 1, 3)
        layout.addWidget(self.canvas, 1, 0, 1, 3)
        layout.addWidget(toolbar2, 2, 0, 1, 3)
        layout.addWidget(self.canvas2, 3, 0, 1, 3)
        layout.addWidget(toolbar3, 4, 0, 1, 3)
        layout.addWidget(self.canvas_3, 5, 0, 1, 3)
        layout.addWidget(self.cb2, 6, 0)
        layout.addWidget(self.cb3, 6, 1)
        layout.addWidget(self.cb, 6, 2)
        layout.addWidget(self.table_of_system_info, 7, 0, 1, 3)

        # Create a placeholder widget to hold the toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        n_data = 15
        # Below is the data for each of the three graphs thats added onto the axis
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

        self.showFullScreen()

        # Set up a timer to trigger the graph to be redrawn by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.time_interval)
        self.timer.timeout.connect(self.update_time)
        self.timer.timeout.connect(self.update_plot_memory_available)
        self.timer.timeout.connect(self.update_plot_CPU_usage)
        # self.timer.timeout.connect(self.update_plot_swap_percent)
        self.timer.timeout.connect(self.change_graph)

        # self.timer.timeout.connect(self.update_plot_bytes_sent)

        self.timer.start()

# All the update plot methods dynamicly change the conense of the graph by clearing the graph with the current
    # points, sotring them and then replotting the whole ting
    def update_plot_memory_available(self):

        self.ydata = self.ydata[1:] + [self.Data_grabber_functions.get_percent_memory()]
        self.xdata = self.xdata[1:] + [self.current_time]
        self.canvas.axes.cla()
        self.canvas.axes.set_title("% RAM used")
        self.canvas.axes.plot(self.xdata, self.ydata, self.color, label="memory")

        self.canvas.draw()

    def update_plot_CPU_usage(self):

        # This method will update the CPU usage graph thiough the import get_total_CPU_usage

        self.ydata2 = self.ydata2[1:] + [self.Data_grabber_functions.get_total_CPU_usage()]
        self.xdata2 = self.xdata2[1:] + [self.current_time]
        self.canvas2.axes.cla()
        self.canvas2.axes.set_title("% CPU used")
        self.canvas2.axes.plot(self.xdata2, self.ydata2, self.color, label="memory")

        self.canvas2.draw()

    def update_plot_bytes_sent(self):

        self.ydata_bytes_sent = self.ydata_bytes_sent[1:] + [self.Data_grabber_functions.get_bytes_sent()]
        self.xdata_bytes_sent = self.xdata_bytes_sent[1:] + [self.current_time]
        self.canvas_3.axes.cla()
        self.canvas_3.axes.set_title("Bytes sent")
        self.canvas_3.axes.plot(self.xdata_bytes_sent, self.ydata_bytes_sent, self.color, label="memory")

        self.canvas_3.draw()

    def update_plot_bytes_recv(self):
        self.ydata_bytes_recv = self.ydata_bytes_recv[1:] + [self.Data_grabber_functions.get_bytes_recv()]
        self.xdata_bytes_recv = self.xdata_bytes_recv[1:] + [self.current_time]
        self.canvas_3.axes.cla()
        self.canvas_3.axes.set_title("Bytes received")
        self.canvas_3.axes.plot(self.xdata_bytes_recv, self.ydata_bytes_recv, self.color, label="memory")

        self.canvas_3.draw()

    def update_plot_swap_percent(self):

        self.ydata_swap_percent = self.ydata_swap_percent[1:] + [self.Data_grabber_functions.get_swap_percent_memory()]
        self.xdata_swap_percent = self.xdata_swap_percent[1:] + [self.current_time]
        self.canvas_3.axes.cla()
        self.canvas_3.axes.set_title("Swap %")
        self.canvas_3.axes.plot(self.xdata_swap_percent, self.ydata_swap_percent, self.color, label="memory")

        self.canvas_3.draw()

    def change_graph(self):
        self.canvas_3_type = self.cb2.currentText()
        self.canvas_3.axes.cla()
        if self.canvas_3_type == "Bytes sent":
            self.update_plot_bytes_sent()
        elif self.canvas_3_type == "Bytes received":
            self.update_plot_bytes_recv()
        elif self.canvas_3_type == "Swap %":
            self.update_plot_swap_percent()

    def changecolor(self):
        self.color = self.cb.currentText()

    def update_time(self):
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")

    def update_time_interval(self):
        self.time_interval = int(self.cb3.currentText())
        self.timer.setInterval(self.time_interval)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()
