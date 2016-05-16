from indicators import *
from register import *
import numpy as np


class zcrIndicator(Indicator):
    fixedBounds = False
    isVoice = 0

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

        (sum, avg, mn, mx) = Indicator.analyse(data)

        ridge_classifier = np.dot([sum, avg, mn, mx], zcrIndicator.coef_) + zcrIndicator.intercept_

        print(ridge_classifier)

        if data.size > 0:
            zcrIndicator.isVoice = 1 if ridge_classifier > 0 else 0
        else:
            zcrIndicator.isVoice = 0
        if data.size > 0:
            with open("logs/anal_zcr.txt", "a+") as f:
                print(str(sum) + "\t" + str(avg) + "\t" + str(mn) + "\t" + str(mx), file=f)

        return data


class zcrIndicator_details:
    print("zcr indicator loaded")
    IndicatorsList.list[Indicators.ZCR] = zcrIndicator

    zcrIndicator.intercept_ = 1.2667888
    # zcrIndicator.intercept_ = 1.05829294
    zcrIndicator.coef_ = [6.03061087e-04, -1.87091677e+00, -1.87091677e+00, -1.87091677e+00]
    # zcrIndicator.coef_ = [6.70199398e-04, -1.73216290e+00, -1.73216290e+00, -1.73216290e+00]
    # zcrIndicator.ridge_classifier =  linear_model.RidgeClassifier(random_state=1)
    # zcrIndicator.ridge_classifier.set_param([[-0.01170097,  0.10515885, -6.70570814,  1.65434725]])
