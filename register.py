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
        print("ADD")
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            # print("ee")
            ui.graphLayouts.removeWidget(gt)
            # l.show()
        # print(ui.verticalLayoutWidget)
        ui.graphLayouts = QVBoxLayout(ui.verticalLayoutWidget)
        dc = MyDynamicMplCanvas(ui.verticalLayoutWidget, width=5, height=4, dpi=100)
        dc.data_process = Register.totalIndicators.get(indic).data_process
        ui.graphLayouts.addWidget(dc)
        # print(dc)
        # ui.invalidate()

        Register.activeIndicators[indic] = dc
        print(Register.activeIndicators)
        dc.show()
        # ui.mywindow.show()
        print("+++ALIST====")
        for i in reversed(range(ui.graphLayouts.count())):
            print(ui.graphLayouts.itemAt(i).widget())
        print("+++ALIST====")

    @staticmethod
    def removeIndicator(indic, ui):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            print("now getL")
            print(gt)
            gt.setParent(None)
            while ui.graphLayouts.count():
                item = ui.graphLayouts.takeAt(0)
                item.widget().deleteLater()
                # ui.graphLayouts.removeWidget(gt)
        # gt.removeWidget()
        # Register.activeIndicators[indic] = 2
        print(Register.activeIndicators)
