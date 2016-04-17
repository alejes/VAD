from indicators.indicators import *
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
