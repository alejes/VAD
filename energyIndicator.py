from indicators import *
from register import *


class energyIndicator(Indicator):
    @staticmethod
    def init():
        pass

    @staticmethod
    def data_process(data):
        return data * 100

    pass


class energyIndicator_details:
    print("energy indicator loaded")
    Register.totalIndicators[Indicators.Energy] = energyIndicator
