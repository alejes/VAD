from indicators import *
from register import *


class energyIndicator(Indicator):
    fixedBounds = True
    boundMin = 0
    boundMax = 50

    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        sum = 0
        for dataFrame in data:
            sum += dataFrame * dataFrame
        data.fill(math.sqrt(sum))
        return data

    pass


class energyIndicator_details:
    print("energy indicator loaded")
    Register.totalIndicators[Indicators.Energy] = energyIndicator
