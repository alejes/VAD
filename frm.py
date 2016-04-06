# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
import FigureCanvasQTAgg
import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from record import *
import random




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStop.setEnabled(False)
        self.pushButtonStop.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.checkBoxWave = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxWave.setGeometry(QtCore.QRect(290, 10, 70, 17))
        self.checkBoxWave.setChecked(True)
        self.checkBoxWave.setAutoRepeat(False)
        self.checkBoxWave.setObjectName("checkBoxWave")
        self.checkBoxEnergy = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxEnergy.setGeometry(QtCore.QRect(350, 10, 70, 17))
        self.checkBoxEnergy.setObjectName("checkBoxEnergy")
        self.checkBoxZCR = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxZCR.setGeometry(QtCore.QRect(430, 10, 70, 17))
        self.checkBoxZCR.setObjectName("checkBoxZCR")
        self.pushButtonPause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPause.setEnabled(False)
        self.pushButtonPause.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.pushButtonPause.setObjectName("pushButtonPause")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuW2w2 = QtWidgets.QMenu(self.menubar)
        self.menuW2w2.setObjectName("menuW2w2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_wave = QtWidgets.QAction(MainWindow)
        self.actionOpen_wave.setObjectName("actionOpen_wave")
        self.actionOpen_wave.setShortcut('Ctrl+O')
        self.actionClose_wave = QtWidgets.QAction(MainWindow)
        self.actionClose_wave.setObjectName("actionClose_wave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_wave = QtWidgets.QAction(MainWindow)
        self.actionSave_wave.setObjectName("actionSave_wave")
        self.actionSave_wave.setShortcut('Ctrl+S')
        self.menuW2w2.addAction(self.actionOpen_wave)
        self.menuW2w2.addAction(self.actionSave_wave)
        self.menuW2w2.addAction(self.actionClose_wave)
        self.menuW2w2.addAction(self.actionExit)
        self.menubar.addAction(self.menuW2w2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        width=5
        height=4
        dpi=100
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        #self.compute_initial_figur()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(object)


        FigureCanvas.updateGeometry(self)
        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent

        self.toolbar = NavigationToolbar(self.canvas, MainWindow)

        # Just some button connected to `plot` method
        #self.button = QtGui.QPushButton('Plot')
        #self.button.clicked.connect(self.plot)

        # set the layout
        #layout = QtGui.QVBoxLayout()
        #layout.addWidget(self.toolbar)
        #layout.addWidget(self.canvas)
        #layout.addWidget(self.button)
        #self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VAD"))
        self.pushButtonStart.setText(_translate("MainWindow", "Start"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop"))
        self.checkBoxWave.setText(_translate("MainWindow", "Wave"))
        self.checkBoxEnergy.setText(_translate("MainWindow", "Energy"))
        self.checkBoxZCR.setText(_translate("MainWindow", "ZCR"))
        self.pushButtonPause.setText(_translate("MainWindow", "Pause"))
        self.menuW2w2.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen_wave.setText(_translate("MainWindow", "Open wave"))
        self.actionClose_wave.setText(_translate("MainWindow", "Close wave"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave_wave.setText(_translate("MainWindow", "Save wave"))

    def ui_prepare(self):
        self.pushButtonStart.clicked.connect(self.startButtonPress)
        self.pushButtonStop.clicked.connect(self.stopButtonPress)
        self.pushButtonPause.clicked.connect(self.pauseButtonPress)
        self.actionSave_wave.triggered.connect(self.saveWaveMenuPress)
        self.actionExit.triggered.connect(sys.exit)

    def startButtonPress(self):
        self.plot()
        self.pushButtonStop.setEnabled(True)
        self.pushButtonStart.setEnabled(False)
        self.pushButtonPause.setEnabled(True)
        print("start")
        runRecord()

    def pauseButtonPress(self):
        self.pushButtonStop.setEnabled(True)
        self.pushButtonStart.setEnabled(True)
        print("pause")
        pauseRecord()

    def stopButtonPress(self):
        self.pushButtonStop.setEnabled(False)
        self.pushButtonStart.setEnabled(True)
        self.pushButtonPause.setEnabled(False)
        print("stio")
        stopRecord()

    def saveWaveMenuPress(self):
        print("Фиг знает, не работает")
        #filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        # filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        # dir = os.path.dirname(os.path.abspath(__file__))
        # filters = "Text files (*.txt);;Images (*.png *.xpm *.jpg)"
        # selected_filter = "Images (*.png *.xpm *.jpg)"
        # options = "" # ???
        # fileObj = QFileDialog.getOpenFileName(self, " File dialog ", dir, filters, selected_filter, options)
        # filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        # filename = QtGui.QFileDialog.getSaveFileName(self,
        #       "Save Address Book", 'C:\\',

        #                "Address Book (*.abk);;All Files (*)")
        # print (filename)
        # def closeEvent(self, event):
        # print("STOP")
        # self.stopButtonPress()


class MyWin(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        stopRecord()

    #def saveWaveMenuPress(self):
        # filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        #print("Фиг знает, не работает")
        # print("eee")
        # filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        # self.label.setText(_translate("MainWindow", filename, None))
