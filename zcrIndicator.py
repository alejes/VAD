from indicators import *
from register import *
import numpy


class zcrIndicator(Indicator):
    fixedBounds = False

    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        cnt = 0
        for i in range(1, data.size - 1):
            if data[i - 1] * data[i] < 0:
                cnt += 1

        data.fill(cnt)

        return data


class waveIndicator_details:
    print("zcr indicator loaded")
    Register.totalIndicators[Indicators.ZCR] = zcrIndicator
