from indicators.indicators import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
print(os.path.join(os.getcwd(), r'register.py'))
from register import *


class waveIndicator(Indicator):
    boundMin = -1
    boundMax = 1

    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        return data

    pass


class waveIndicator_details:
    print("wave indicator loaded")
    IndicatorsList.list[Indicators.Wave] = waveIndicator
