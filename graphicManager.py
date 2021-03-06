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
# from graphic import *
import threading
# from register import *
import register as reg
from record import *


class GraphicManager:
    def __init__(self, *args, **kwargs):
        self.t = threading.Timer(1.0, self.manager, ())
        self.t.start()
        print("maked timer")

    def manager(self):
        # print("manager tick")
        # print(Record.getTime())
        while True:
            currentTime = Record.getTime()

            startTime = time.clock()

            try:
                for ind in reg.Register.activeIndicators.values():
                    if ind.getName() != "wave":
                        ind.data_update()
                for ind in reg.Register.activeIndicators.values():
                    if ind.getName() == "wave":
                        ind.data_update()
                for ind in reg.Register.activeIndicators.values():
                    ind.update_figure(currentTime)

                for ind in reg.Register.activeIndicators.values():
                    if ind.active:
                        ind.release_figure()

            except RuntimeError:
                # dictionary changed size
                pass

            endTime = time.clock()
            #print(endTime - startTime)
            if endTime - startTime < 0.1:
                self.t = threading.Timer(0.1, self.manager, ())
                self.t.start()
                break
        #
