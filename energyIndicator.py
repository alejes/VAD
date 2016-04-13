from indicators import *
from register import *


class energyIndicator(Indicator):
    fixedBounds = False
    @staticmethod
    def init():
        pass
    @staticmethod
    def data_process(data):
        sum = 0
        for dataFrame in data:
            sum += dataFrame * dataFrame
        data.fill(sum)
        return data

    pass


class energyIndicator_details:
    print("energy indicator loaded")
    Register.totalIndicators[Indicators.Energy] = energyIndicator
