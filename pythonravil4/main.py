#!/usr/bin/env python3
# coding=utf-8

import sys
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui
import random
import math

class Example(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.table = QTableWidget(self)
        btn1 = QPushButton("Заполнить", self)
        btn2 = QPushButton("Выполнить ", self)
        btn3 = QPushButton("Очистить", self)
        btn4 = QPushButton("Выход", self)
        self.label = QLabel(self)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.table.setGeometry(10, 10, 250, 360)
        btn1.setGeometry(270, 280, 140, 40)
        btn2.setGeometry(270, 330, 140, 40)
        btn3.setGeometry(420, 280, 140, 40)
        btn4.setGeometry(420, 330, 140, 40)
        self.label.setGeometry(270, 10, 500, 260)

        self.table.setColumnCount(2)     
        self.table.setRowCount(10)        

        pixmap = QPixmap('Zadanie4.jpg')
        self.label.setPixmap(pixmap)

        btn1.clicked.connect(self.btn1Click)
        btn2.clicked.connect(self.btn2Click)
        btn3.clicked.connect(self.btn3Click)
        btn4.clicked.connect(self.btn4Click)

        self.setGeometry(300, 300, 780, 380)
        self.setWindowTitle('Test')
        self.show()

    def btn1Click(self):
        y = 0
        while y < 10:
            self.table.setItem(y, 0, QTableWidgetItem(str(random.randint(-99,99))))
            y = y + 1

    def btn2Click(self):
        sum = 0
        proizv = 1

        y = 0
        while y < 10:
            v = int(self.table.item(y, 0).text())
            sum = sum + v
            proizv = proizv * v
            y = y + 1

        y = 0
        while y < 10:
            print(y)
            v = int(self.table.item(y, 0).text())
            r = 0
            r = (math.sin(v)-math.sin(v-1))/math.sin(v-(v-1))/2
            sss = "% 10.8f" % r
            self.table.setItem(y, 1, QTableWidgetItem(sss))
            y = y + 1

    def btn3Click(self):
        y = 0
        while y < 10:
            self.table.setItem(y, 1, QTableWidgetItem(""))
            y = y + 1

    def btn4Click(self):
        QApplication.exit()

if __name__=='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
