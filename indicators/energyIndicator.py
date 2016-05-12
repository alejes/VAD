from indicators import *
from register import *
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
        sum = 0
        haveVoice = False
        for dataFrame in data:
            sum += dataFrame * dataFrame
            if dataFrame > energyIndicator.thresholdOnce:
                haveVoice = True

        if sum > energyIndicator.thresholdTotal:
            haveVoice = True

        energyIndicator.maxEnergy.append(math.sqrt(sum))

        currentMaxEnergy = max(1, max(energyIndicator.maxEnergy))

        if currentMaxEnergy > 0:
            data.fill(math.sqrt(sum) / currentMaxEnergy)
        else:
            data.fill(math.sqrt(sum))

        energyIndicator.isVoice = 4 if haveVoice else 0
        return data

    pass


class energyIndicator_details:
    print("energy indicator loaded")
    IndicatorsList.list[Indicators.Energy] = energyIndicator
