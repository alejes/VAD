from indicators.indicators import *
from register import *


class waveIndicator(Indicator):
    boundMin = -1
    boundMax = 1
    isVoice = 0

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
        (sum, avg, mn, mx) = Indicator.analyse(data)
        if data.size > 0:
            with open("logs/anal_wave.txt", "a+") as f:
                print(str(sum) + "\t" + str(avg) + "\t" + str(mn) + "\t" + str(mx), file=f)
        return data

    pass


class waveIndicator_details:
    print("wave indicator loaded")
    IndicatorsList.list[Indicators.Wave] = waveIndicator
