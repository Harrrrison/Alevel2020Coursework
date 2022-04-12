from PyQt5 import uic, QtWidgets, QtGui, QtSql, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from Scripts.LogIn import *
import sys
import os
import hashlib
import sqlite3
from sqlCode import *

class database(QtWidgets):
    def __init__(self):
        #self.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("DataMonitor")
        self.db.setDatabaseName("UserDetails")
        self.db.setUserName("Harrison")
        self.db.setPassword("123456")
        # self.qry = QString("SELECT * FROM employee")
        # self.query = QSqlQuery()
        self.query.prepare(self.qry)
        self.query.exec()

