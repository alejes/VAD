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

    @staticmethod
    def analyse(dic):
        if dic.size == 0:
            return (0, 0, 10000, -10000)
        sum = 0
        mx = dic[0]
        mn = dic[0]
        avg = 0
        for value in dic:
            sum += value
            mx = max(mx, value)
            mn = min(mn, value)
        avg = 1.0 * sum / dic.size
        return (sum, avg, mn, mx)

class IndicatorsList:
    list = {}
