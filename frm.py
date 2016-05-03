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
from graphic import *
import shutil
import os.path
from register import *
from indicators import *
import random
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random


class Ui_MainWindow(object):
    initialWidth = 500
    graphHeight = 400

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, self.initialWidth)
        self.mywindow = MainWindow
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
        self.checkBoxZCR.setGeometry(QtCore.QRect(410, 10, 70, 17))
        self.checkBoxZCR.setObjectName("checkBoxZCR")
        self.checkBoxMFCC = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxMFCC.setGeometry(QtCore.QRect(470, 10, 70, 17))
        self.checkBoxMFCC.setObjectName("checkBoxMFCC")
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

        self.verticalLayoutWidget = {}
        self.verticalLayout = {}
        self.graphLayouts = {}

        # l = QVBoxLayout(self.centralwidget)
        # dc = MyDynamicMplCanvas(self.centralwidget, width=5, height=4, dpi=100)
        # l.addWidget(sc)
        # l.addWidget(dc)
        ##l.addWidget(dc)

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
        self.checkBoxMFCC.setText(_translate("MainWindow", "MFCC"))
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
        self.actionSave_wave.triggered.connect(self.mywindow.saveWaveMenuPress)
        self.actionOpen_wave.triggered.connect(self.mywindow.openWaveMenuPress)
        self.actionClose_wave.triggered.connect(self.mywindow.closeWaveMenuPress)
        self.actionExit.triggered.connect(sys.exit)
        self.checkBoxWave.clicked.connect(self.waveCheckBoxPress)
        self.checkBoxEnergy.clicked.connect(self.energyCheckBoxPress)
        self.checkBoxZCR.clicked.connect(self.zcrCheckBoxPress)
        self.checkBoxMFCC.clicked.connect(self.mfccCheckBoxPress)

        Register.addIndicator(Indicators.Wave, self, True)
        Register.addIndicator(Indicators.MFCC, self, False)
        Register.addIndicator(Indicators.Energy, self, False)
        Register.addIndicator(Indicators.ZCR, self, False)
        Record.ui = self

    def waveCheckBoxPress(self):
        if self.checkBoxWave.isChecked():
            Register.switchOn(Indicators.Wave, self)
        else:
            Register.switchOff(Indicators.Wave, self)

    def energyCheckBoxPress(self):
        if self.checkBoxEnergy.isChecked():
            Register.switchOn(Indicators.Energy, self)
        else:
            Register.switchOff(Indicators.Energy, self)

    def zcrCheckBoxPress(self):
        if self.checkBoxZCR.isChecked():
            Register.switchOn(Indicators.ZCR, self)
        else:
            Register.switchOff(Indicators.ZCR, self)

    def mfccCheckBoxPress(self):
        if self.checkBoxMFCC.isChecked():
            Register.switchOn(Indicators.MFCC, self)
        else:
            Register.switchOff(Indicators.MFCC, self)

    def startButtonPress(self):
        self.pushButtonStop.setEnabled(True)
        self.pushButtonStart.setEnabled(False)
        self.pushButtonPause.setEnabled(True)
        print("start")
        Record.runRecord()

    def pauseButtonPress(self):
        self.pushButtonStop.setEnabled(True)
        self.pushButtonStart.setEnabled(True)
        print("pause")
        Record.pauseRecord()

    def stopButtonPress(self):
        self.pushButtonStop.setEnabled(False)
        self.pushButtonStart.setEnabled(True)
        self.pushButtonPause.setEnabled(False)
        print("stio")
        Record.stopRecord()


class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumHeight(200)
        self.setMinimumWidth(523)

    def closeEvent(self, event):
        Record.stopRecord()
        Register.Truncate(self)
        GraphicManager.t.cancel()

    def updateGraphsLocations(self):
        currentSize = self._ui.mywindow.size()

        # print("resize " + str(time.time()))
        cntActive = 0
        for widgetKey in Register.activeIndicators:
            if Register.activeIndicators[widgetKey].active:
                cntActive += 1

        if cntActive > 0:
            singleHeight = math.floor(
                (currentSize.height() - 40) / cntActive)

        id = 0
        for widgetKey in Register.activeIndicators:
            if Register.activeIndicators[widgetKey].active:
                Register.activeIndicators[widgetKey].resize(currentSize.width(), singleHeight - 50)
                self._ui.verticalLayoutWidget[widgetKey].setGeometry(
                    QtCore.QRect(10, 40 + singleHeight * id, 6510, 3810))
                id += 1

    def resizeEvent(self, resizeEvent):
        # print(resizeEvent.size())
        self.updateGraphsLocations()

    def saveWaveMenuPress(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file', QtCore.QDir.homePath(), "Wave Files (*.wav), *.wav")
        if fname[0]:
            shutil.copyfile(QtCore.QDir.currentPath() + '/output.wav', fname[0])

    def openWaveMenuPress(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', QtCore.QDir.homePath(), "Wave Files (*.wav), *.wav")
        if fname[0]:
            if os.path.isfile(fname[0]):
                Record.stopRecord()
                Record.source = fname[0]

    def closeWaveMenuPress(self):
        Record.source = None
        Record.stopRecord()
        Register.Truncate(self)
