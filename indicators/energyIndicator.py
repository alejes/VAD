from indicators import *
from register import *
from collections import deque
import math


class energyIndicator(Indicator):
    fixedBounds = True
    boundMin = 0
    boundMax = 1
    maxEnergy = deque(maxlen=25)

    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        sum = 0
        for dataFrame in data:
            sum += dataFrame * dataFrame

        energyIndicator.maxEnergy.append(math.sqrt(sum))

        currentMaxEnergy = max(1, max(energyIndicator.maxEnergy))

        if currentMaxEnergy > 0:
            data.fill(math.sqrt(sum) / currentMaxEnergy)
        else:
            data.fill(math.sqrt(sum))

        return data

    data_process.name = "energy"
    pass


class energyIndicator_details:
    print("energy indicator loaded")
    IndicatorsList.list[Indicators.Energy] = energyIndicator
