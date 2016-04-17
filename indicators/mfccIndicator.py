from indicators import *
from register import *
import numpy


class mfccIndicator(Indicator):
    boundMin = -1
    boundMax = 1

    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        return data

    pass


class mfccIndicator_details:
    print("mfcc indicator loaded")
    IndicatorsList.list[Indicators.MFCC] = waveIndicator
