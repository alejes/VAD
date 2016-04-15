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
from graphicManager import *


class Register:
    activeIndicators = {}
    totalIndicators = {}
    position = 0
    graphicManager = GraphicManager()

    @staticmethod
    def addIndicator(indic, ui):
        print("ADD")
        # currentSize = ui.mywindow.size()
        # currentSize.setHeight(ui.initialWidth + ui.graphHeight * (len(ui.verticalLayoutWidget) + 1))
        # ui.mywindow.resize(currentSize)

        ui.verticalLayoutWidget[indic] = QtWidgets.QWidget(ui.centralwidget)
        ui.verticalLayoutWidget[indic].setGeometry(
            QtCore.QRect(10, 40 + ui.graphHeight * (len(ui.verticalLayoutWidget) - 1), 6510, 3810))
        ui.verticalLayoutWidget[indic].setObjectName("verticalLayoutWidget")
        ui.verticalLayout[indic] = QtWidgets.QVBoxLayout(ui.verticalLayoutWidget[indic])
        ui.verticalLayout[indic].setObjectName("verticalLayout")
        ui.graphLayouts[indic] = QVBoxLayout(ui.verticalLayoutWidget[indic])

        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            ui.graphLayouts.removeWidget(gt)
        ui.graphLayouts[indic] = QVBoxLayout(ui.verticalLayoutWidget[indic])
        dc = MyDynamicMplCanvas(ui.verticalLayoutWidget[indic], width=5, height=4, dpi=100)

        currentTotalIndic = Register.totalIndicators.get(indic)

        dc.data_process = currentTotalIndic.data_process
        dc.updateTime = currentTotalIndic.updateTime
        dc.fixedBounds = currentTotalIndic.fixedBounds
        if "boundMin" in currentTotalIndic.__dict__:
            dc.boundMin = currentTotalIndic.boundMin
        if "boundMax" in currentTotalIndic.__dict__:
            dc.boundMax = currentTotalIndic.boundMax

        ui.graphLayouts[indic].addWidget(dc)

        Register.activeIndicators[indic] = dc
        ui.verticalLayoutWidget[indic].show()
        dc.show()
        ui.mywindow.updateGraphsLocations()

    @staticmethod
    def removeIndicator(indic, ui):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            ui.verticalLayoutWidget[indic].setParent(None)
            ui.verticalLayoutWidget.pop(indic)
        ui.mywindow.updateGraphsLocations()
