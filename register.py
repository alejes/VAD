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
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            ui.graphLayouts.removeWidget(gt)
        ui.graphLayouts[Register.position] = QVBoxLayout(ui.verticalLayoutWidget[Register.position])
        dc = MyDynamicMplCanvas(ui.verticalLayoutWidget[Register.position], width=5, height=4, dpi=100)
        dc.data_process = Register.totalIndicators.get(indic).data_process
        ui.graphLayouts[Register.position].addWidget(dc)
        Register.position+=1

        Register.activeIndicators[indic] = dc
        dc.show()

    @staticmethod
    def removeIndicator(indic, ui):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            gt.setParent(None)
            while ui.graphLayouts.count():
                item = ui.graphLayouts.takeAt(0)
                item.widget().deleteLater()