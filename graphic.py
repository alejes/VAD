import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QSizePolicy)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from record import *
from details_classes import *
import numpy
import random
import collections


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), facecolor='none', dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_ybound(lower=-1, upper=1)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

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
        timer.start(100)
        self._currentId = Record.getCurrentId()
        self.data = numpy.array([])

    def compute_initial_figure(self):
        pass

    def update_figure(self):
        if Record.recordState == RecordStates.Run:
            beginid = self._currentId
            newid = Record.getCurrentId()
            data = Record.getDataFromTo(self._currentId, newid)
            self._currentId = newid

            data = b''.join(data)
            data = numpy.fromstring(data, numpy.int16) / Record.AMPLITUDE

            if "data_process" in self.__dict__:
                data = self.data_process(data)

            self.data = numpy.concatenate((self.data, data))

            plottingSize = min(self.plotDataSize, self.data.size)
            self.axes.plot([x for x in frange(Record.CHUNK * beginid / Record.RATE, plottingSize, 1.0 / Record.RATE)],
                           self.data[-plottingSize:], 'g')
            # self.axes.patch.set_facecolor('blue')
            # self.axes.grid(True)
            if "fixedBounds" not in self.__dict__ or self.fixedBounds:
                self.axes.set_ybound(lower=-1, upper=1)
            else:
                self.axes.set_ybound(lower=0)


            self.draw()
