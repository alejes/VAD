#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMenu, QVBoxLayout,
                             QSizePolicy, QMessageBox, QWidget)

from PyQt5.QtGui import QIcon
from record import *
import shutil
import random
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.__mywindow = MainWindow
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

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 651, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        l = QVBoxLayout(self.verticalLayoutWidget)
        dc = MyDynamicMplCanvas(self.verticalLayoutWidget, width=5, height=4, dpi=100)
        l.addWidget(dc)

        #self.main_widget.setFocus()


        #self.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.actionSave_wave.triggered.connect(self.__mywindow.saveWaveMenuPress)
        self.actionExit.triggered.connect(sys.exit)

    def startButtonPress(self):
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


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class MyDynamicMplCanvas(MyMplCanvas):
  """A canvas that updates itself every second with a new plot."""
  def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

  def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

  def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()


class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)



    def closeEvent(self, event):
        stopRecord()

    def saveWaveMenuPress(self):
        fname = QFileDialog.getSaveFileName(self, 'Open file', QtCore.QDir.homePath(), "Wave Files (*.wav), *.wav")
        if fname[0]:
            shutil.copyfile(QtCore.QDir.currentPath() + '/output.wav', fname[0])
