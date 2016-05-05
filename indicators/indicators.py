from enum import Enum


class Indicators(Enum):
    Wave = 0
    Energy = 1
    ZCR = 2
    MFCC = 3


class Indicator:
    updateTime = 10
    fixedBounds = True

    @staticmethod
    def getName():
        return "undefined"

    pass


class IndicatorsList:
    list = {}
