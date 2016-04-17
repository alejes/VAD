from enum import Enum


class Indicators(Enum):
    Wave = 0
    Energy = 1
    ZCR = 2


class Indicator:
    updateTime = 10
    fixedBounds = True
    pass


class IndicatorsList:
    list = {}
