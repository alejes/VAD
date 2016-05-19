from indicators import *
from register import *
import numpy as np
from collections import deque
import math


class energyIndicator(Indicator):
    fixedBounds = True
    boundMin = 0
    boundMax = 1
    maxEnergy = deque(maxlen=25)
    isVoice = 0

    @staticmethod
    def getVoiceStatus():
        return energyIndicator.isVoice

    @staticmethod
    def getName():
        return "energy"

    @staticmethod
    def init():
        pass

    thresholdOnce = 0.02
    thresholdTotal = 0.02

    @staticmethod
    def data_process(data):
        sumSquare = 0
        haveVoice = False
        for dataFrame in data:
            sumSquare += dataFrame * dataFrame
            if dataFrame > energyIndicator.thresholdOnce:
                haveVoice = True

        if sumSquare > energyIndicator.thresholdTotal:
            haveVoice = True

        energyIndicator.maxEnergy.append(math.sqrt(sumSquare))

        currentMaxEnergy = max(1, max(energyIndicator.maxEnergy))

        if currentMaxEnergy > 0:
            data.fill(math.sqrt(sumSquare) / currentMaxEnergy)
        else:
            data.fill(math.sqrt(sumSquare))

        # energyIndicator.isVoice = 4 if haveVoice else 0

        (sum, avg, mn, mx) = Indicator.analyse(data)

        ridge_classifier = np.dot([sum, avg, mn, mx], energyIndicator.coef_) + energyIndicator.intercept_

        if data.size > 0:
            energyIndicator.isVoice = 1 if ridge_classifier > 0 else 0
        else:
            energyIndicator.isVoice = 0

        if not haveVoice:
            energyIndicator.isVoice = -10

        if data.size > 0:
            with open("logs/anal_energy.txt", "a+") as f:
                print(str(sum) + "\t" + str(avg) + "\t" + str(mn) + "\t" + str(mx), file=f)

        return data

    pass


class energyIndicator_details:
    print("energy indicator loaded")
    IndicatorsList.list[Indicators.Energy] = energyIndicator
    energyIndicator.intercept_ = -0.43582075
    # energyIndicator.intercept_ = -0.53095882
    energyIndicator.coef_ = [-5.19400273e-05, 7.44976464e-01, 7.44976464e-01, 7.44976464e-01]
    # energyIndicator.coef_ = [1.64026857e-04, 5.83134532e-01, 5.83134532e-01, 5.83134532e-01]
