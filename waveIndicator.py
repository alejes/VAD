from indicators import *
from register import *


class waveIndicator(Indicator):
    @staticmethod
    def init():
        pass
    pass

class details_reg:
    print("***")
    Register.totalIndicators[Indicators.Wave] = waveIndicator