from indicators import *
from register import *
import numpy as np


class autocIndicator(Indicator):
    fixedBounds = False
    isVoice = 0

    @staticmethod
    def getVoiceStatus():
        return autocIndicator.isVoice

    @staticmethod
    def getName():
        return "autoc"

    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        cnt = 0
        # print(str(data.size) + "===")
        if data.size > 0:
            result = numpy.correlate(data, data, mode='full')
            data = result[result.size / 2:]
            # print(str(data.size) + "===" + str(result.size))

        (sum, avg, mn, mx) = Indicator.analyse(data)

        ridge_classifier = np.dot([sum, avg, mn, mx], autocIndicator.coef_) + autocIndicator.intercept_

        if data.size > 0:
            autocIndicator.isVoice = 0 if ridge_classifier > 0 else 0
        else:
            autocIndicator.isVoice = 0

        if data.size > 0:
            with open("logs/anal_autoc.txt", "a+") as f:
                print(str(sum) + "\t" + str(avg) + "\t" + str(mn) + "\t" + str(mx), file=f)

        return data


class autocorrIndicator_details:
    print("autoc indicator loaded")
    IndicatorsList.list[Indicators.AUTOC] = autocIndicator

    autocIndicator.intercept_ = 0.59867863
    autocIndicator.coef_ = [-0.15975306, 0.0412668, -0.41195572, -0.15356962]
