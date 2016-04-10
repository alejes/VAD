from enum import Enum


class RecordStates(Enum):
    Stop = 0
    Run = 1
    Pause = 2


def frange(x, lenght, jump):
    while lenght > 0:
        yield x
        x += jump
        lenght -= 1
