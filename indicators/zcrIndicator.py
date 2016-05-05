from indicators import *
from register import *
import numpy


class zcrIndicator(Indicator):
    fixedBounds = False
    isVoice = False

    @staticmethod
    def getVoiceStatus():
        return zcrIndicator.isVoice

    @staticmethod
    def getName():
        return "zcr"

    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        cnt = 0
        for i in range(1, data.size - 1):
            if data[i - 1] * data[i] < 0:
                cnt += 1

        if data.size > 0:
            data.fill(cnt * 1.0 / data.size)

        return data


class waveIndicator_details:
    print("zcr indicator loaded")
    IndicatorsList.list[Indicators.ZCR] = zcrIndicator
