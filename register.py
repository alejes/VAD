import matplotlib

matplotlib.use("Qt5Agg")
import pyaudio
import wave
import threading
import numpy
from details_classes import *
from indicators import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QSizePolicy)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMenu, QVBoxLayout,
                             QSizePolicy, QMessageBox, QWidget)
from PyQt5.QtCore import (QRect)
from graphic import *


class Register:
    activeIndicators = {}
    totalIndicators = {}
    position = 0

    @staticmethod
    def addIndicator(indic, ui):
        print("ADD")
        currentSize = ui.mywindow.size()
        currentSize.setHeight(currentSize.height() + 400)
        ui.mywindow.resize(currentSize)

        ui.verticalLayoutWidget[indic] = QtWidgets.QWidget(ui.centralwidget)
        ui.verticalLayoutWidget[indic].setGeometry(
            QtCore.QRect(10, 40 + 400 * (len(ui.verticalLayoutWidget) - 1), 651, 381))
        ui.verticalLayoutWidget[indic].setObjectName("verticalLayoutWidget")
        ui.verticalLayout[indic] = QtWidgets.QVBoxLayout(ui.verticalLayoutWidget[indic])
        ui.verticalLayout[indic].setObjectName("verticalLayout")
        ui.graphLayouts[indic] = QVBoxLayout(ui.verticalLayoutWidget[indic])

        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            ui.graphLayouts.removeWidget(gt)
        ui.graphLayouts[indic] = QVBoxLayout(ui.verticalLayoutWidget[indic])
        dc = MyDynamicMplCanvas(ui.verticalLayoutWidget[indic], width=5, height=4, dpi=100)
        dc.data_process = Register.totalIndicators.get(indic).data_process
        ui.graphLayouts[indic].addWidget(dc)
        # Register.position+=1

        Register.activeIndicators[indic] = dc
        ui.verticalLayoutWidget[indic].show()
        dc.show()

    @staticmethod
    def removeIndicator(indic, ui):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            botWidth = ui.verticalLayoutWidget[indic].geometry().bottomLeft().y()
            ui.verticalLayoutWidget[indic].setParent(None)
            ui.verticalLayoutWidget.pop(indic)
            for key in ui.verticalLayoutWidget.keys():
                print("BEFORE")
                print(ui.verticalLayoutWidget[key].geometry())
                currentRect = ui.verticalLayoutWidget[key].geometry().getRect()

                if currentRect[1] > botWidth:
                    currentRect = QRect(currentRect[0], currentRect[1] - 400, currentRect[2], currentRect[3])
                    ui.verticalLayoutWidget[key].setGeometry(currentRect)

                print(ui.verticalLayoutWidget[key].geometry())
                # print(values.geometry())
                ui.verticalLayoutWidget[key].show()
                # currentSize = ui.mywindow.size()
                # currentSize.setHeight(currentSize.height() - 400)
                # ui.mywindow.resize(currentSize)
                # gt.setParent(None)
                # while ui.graphLayouts.count():
                #   item = ui.graphLayouts.takeAt(0)
                # item.widget().deleteLater()
