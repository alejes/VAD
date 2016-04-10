import pyaudio
import wave
import threading
import matplotlib.pyplot as plt
import numpy
from details_classes import *
from indicators import *


class Register:
    activeIndicators = {}
    totalIndicators = {}

    @staticmethod
    def addIndicator(indic):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            pass
        Register.activeIndicators[indic] = Register.totalIndicators.get(indic)
        print(Register.activeIndicators)

    @staticmethod
    def removeIndicator(indic):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            pass
        # Register.activeIndicators[indic] = 2
        print(Register.activeIndicators)
