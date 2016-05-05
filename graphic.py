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
import math


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(facecolor='none', dpi=dpi)
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
        self.resize(1000, 200)

    def compute_initial_figure(self):
        pass


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        # timer = QtCore.QTimer(self)
        # timer.timeout.connect(self.update_figure)
        # timer.start(10)
        self._currentId = Record.getCurrentId()
        self.data = numpy.array([])
        self.VADdata = numpy.array([])
        self.secondsLen = 10
        self.dataSpeed = 1

    def compute_initial_figure(self):
        pass

    def data_update(self):
        if Record.recordState == RecordStates.Run:
            newid = Record.getCurrentId()
            data = Record.getDataFromTo(self._currentId, newid)
            self._currentId = newid

            data = b''.join(data)
            try:
                data = numpy.fromstring(data, numpy.int16) / Record.AMPLITUDE
            except:
                data = numpy.array([])
            if "data_process" in self.__dict__:
                originalSize = data.size
                data = self.data_process(data).flatten()
                if data.size > 0 and originalSize > 0:
                    self.dataSpeed = originalSize / data.size
            # print("concat: " + str(self.data.size) + " size=" + str(data.size))

            self.data = numpy.concatenate((self.data, data))
            if self.getName() == "wave":
                releaseVAD = self.evaluateVad()
                VADdata = data
                VADdata.fill(0.5 if releaseVAD else 0)
                self.VADdata = numpy.concatenate((self.VADdata, VADdata))

    def update_figure(self, currentTime):
        if Record.recordState == RecordStates.Run:
            # plotStartId = self.secondsLen * Record.RATE
            plotStartSec = math.floor(max(currentTime - self.secondsLen, 0) / 2) * 2

            # print(str(math.floor(plotStartSec * Record.RATE / self.dataSpeed)) + ":" + str(
            #   math.floor(currentTime * Record.RATE / self.dataSpeed)))

            data = self.data[math.floor(plotStartSec * Record.RATE / self.dataSpeed):math.floor(
                currentTime * Record.RATE / self.dataSpeed)]

            if self.getName() == "wave":
                VADdata = self.VADdata[math.floor(plotStartSec * Record.RATE / self.dataSpeed):math.floor(
                    currentTime * Record.RATE / self.dataSpeed)]

            if data.size > 0:
                delta = (currentTime - plotStartSec) * 1.0 / data.size
            else:
                delta = 1

            # print("plotStartSec = " + str(plotStartSec)  + " Record.RATE="  +str(Record.RATE) + "  self.dataSpeed=" + str(self.dataSpeed) + " currentTime =" + str(currentTime ) + " delta = " + str(delta) )
            # print(data)
            # print(self.axes.transAxes)
            # plottingSize = min(self.plotDataSize, self.data.size)

            # self.axes.hold(False)
            self.axes.hold(True)
            self.axes.clear()
            self.axes.plot([x for x in frange(plotStartSec, data.size, delta)],
                           data, 'g')

            fig, ax = plt.subplots(1, 1)
            #            ax.set_xticks(data.size) # set tick positions

            if self.getName() == "wave":
                self.axes.plot([x for x in frange(plotStartSec, VADdata.size, delta)], VADdata, 'r')


                # pass
            # self.axes.patch.set_facecolor('blue')
            # self.axes.grid(True)
            if "fixedBounds" not in self.__dict__ or self.fixedBounds:
                if "boundMax" in self.__dict__:
                    self.axes.set_ybound(lower=self.boundMin, upper=self.boundMax)
                else:
                    self.axes.set_ybound(lower=-1, upper=1)
            else:
                self.axes.set_ybound(lower=0)

    def evaluateVad(self):
        cntTrue = 0
        for ind in self.activeIndicators.values():
            if ind.getVoiceStatus():
                cntTrue += 1
        Record.VADstatus = cntTrue > 0
        return Record.VADstatus

    def release_figure(self):
        self.draw()
