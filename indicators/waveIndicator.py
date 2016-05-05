from indicators.indicators import *
from register import *


class waveIndicator(Indicator):
    boundMin = -1
    boundMax = 1
    isVoice = False

    @staticmethod
    def getVoiceStatus():
        return waveIndicator.isVoice

    @staticmethod
    def getName():
        return "wave"

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
