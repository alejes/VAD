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
                             QGridLayout, QPushButton,
                             QSizePolicy, QMessageBox, QWidget)
from graphic import *


class Register:
    activeIndicators = {}
    totalIndicators = {}
    position = 0

    @staticmethod
    def addIndicator(indic, ui):
        print("ADD")
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            ui.graphLayouts.removeWidget(gt)

        dc = MyDynamicMplCanvas(ui.verticalLayoutWidget, width=5, height=4, dpi=100)
        dc.data_process = Register.totalIndicators.get(indic).data_process

        ui.graphLayouts.addWidget(dc, Register.position, 0)
        Register.position += 1

        Register.activeIndicators[indic] = dc
        dc.show()

        for i in range(ui.graphLayouts.count()):
            print(ui.graphLayouts.itemAt(i))

    @staticmethod
    def removeIndicator(indic, ui):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            gt.setParent(None)
            while ui.graphLayouts.count():
                item = ui.graphLayouts.takeAt(0)
                item.widget().deleteLater()
