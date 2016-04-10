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

    @staticmethod
    def addIndicator(indic, ui):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            #print("ee")
            ui.graphLayouts.removeWidget(gt)
            # l.show()
        dc = MyDynamicMplCanvas(ui.verticalLayoutWidget, width=5, height=4, dpi=100)
        dc.data_process = Register.totalIndicators.get(indic).data_process
        ui.graphLayouts.addWidget(dc)
        #dc = MyDynamicMplCanvas(ui.verticalLayoutWidget, width=5, height=4, dpi=100)
        #l.addWidget(dc)
        Register.activeIndicators[indic] = dc
        print(Register.activeIndicators)

    @staticmethod
    def removeIndicator(indic, ui):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            ui.graphLayouts.removeWidget(gt)
#            gt.removeWidget()
        # Register.activeIndicators[indic] = 2
        print(Register.activeIndicators)
