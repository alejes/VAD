#!/usr/bin/python3
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
from PyQt5.QtGui import QIcon
from record import *
#import PyQtGraph

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

    #def saveWaveMenuPress(self):
        #print("Фиг знает, не работает")
        #filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        #print("223")
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


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def closeEvent(self, event):
        stopRecord()

    def saveWaveMenuPress(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', QtCore.QDir.homePath())

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)
        #filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.homePath(self),"")
        # def saveWaveMenuPress(self):
        # filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        # print("Фиг знает, не работает")
        # print("eee")
        # filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        # self.label.setText(_translate("MainWindow", filename, None))
