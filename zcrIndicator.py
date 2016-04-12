from indicators import *
from register import *


class zcrIndicator(Indicator):
    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        return data*300

    pass


class waveIndicator_details:
    print("wave indicator loaded")
    Register.totalIndicators[Indicators.ZCR] = zcrIndicator
