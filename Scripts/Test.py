import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from Data_grabber_functions import *


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
        table_data = []

        data = [self.Data_grabber_functions.get_system_name(), self.Data_grabber_functions.get_system_node(),
                self.Data_grabber_functions.get_system_release(),
                self.Data_grabber_functions.get_system_version(),
                self.Data_grabber_functions.get_system_machine(),
                self.Data_grabber_functions.get_system_processor()]

        table_data.append(data)

        row = 0
        for r in table_data:
            col = 0
            for item in r:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1
            row += 1
        vbox.addWidget(table)
        self.setLayout(vbox)
        self.setGeometry(300, 400, 500, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = partsTable()
    sys.exit(app.exec())
