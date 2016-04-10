import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QSizePolicy)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from record import *
from details_classes import *
import random


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_ybound(lower=-1,upper=1)
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

    def compute_initial_figure(self):
        pass
        # self.axes.plot([0, 1, 2, 3], [0, 0, 0, 0, 'r')
        #self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')
        #self.axis('off')
        #self.axes.autoscale(self, False)
        #r = int(10 * random.random())
        #self.axis.set_xlabel(str(r))

    def update_figure(self):
        if Record.recordState == RecordStates.Run:
            # Build a list of 4 random integers between 0 and 10 (both inclusive)
            # l = [random.randint(0, 10) for i in range(4)]
            beginid = self._currentId
            newid = Record.getCurrentId()
            data = Record.getDataFromTo(self._currentId, newid)
            self._currentId = newid

            data = b''.join(data)
            data = numpy.fromstring(data, numpy.int16) / Record.AMPLITUDE
            # print( Record.AMPLITUDE)
            print("CurrentId = " + str(beginid) + " next = " + str(Record.getCurrentId()))
            # print(data)
            # print(data.size)
            print(beginid / Record.RATE)

            # print([x for x in frange(beginid / Record.RATE, data.size, 1.0 / Record.RATE)])

            self.axes.plot([x for x in frange(Record.CHUNK * beginid / Record.RATE, data.size, 1.0 / Record.RATE)],
                           data, 'r')
            self.axes.set_ybound(lower=-1,upper=1)
            self.draw()
