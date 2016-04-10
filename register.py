import pyaudio
import wave
import threading
import matplotlib.pyplot as plt
import numpy
from details_classes import *


class Indicator(Enum):
    Wave = 0
    Energy = 1
    ZCR = 2


class Register:
    activeIndicators = {}

    @staticmethod
    def addIndicator(indic):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            pass
        Register.activeIndicators[indic] = 1
        print(Register.activeIndicators)

    @staticmethod
    def removeIndicator(indic):
        gt = Register.activeIndicators.pop(indic, None)
        if gt is not None:
            pass
        # Register.activeIndicators[indic] = 2
        print(Register.activeIndicators)
