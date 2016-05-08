import pyaudio
import wave
import threading
import matplotlib.pyplot as plt
import numpy
import math
from details_classes import *
import time


class Record:
    # сам тред записи
    recordThread = None
    # текущее состояние треда
    recordState = RecordStates.Stop
    # флаг НЕ активности паузы
    pauseEventRunState = threading.Event()
    # записываемые данные
    _frames = []
    _clear_frames = []
    RATE = 8000
    CHUNK = 512
    AMPLITUDE = 2 ** 15
    startTime = time.clock()
    deltaTime = time.clock()
    source = None
    ui = None
    VADstatus = False

    @staticmethod
    def getTime():
        delta = (time.clock() - Record.deltaTime)
        return time.clock() - Record.startTime - (delta if Record.deltaTime > 0 else 0)

    @staticmethod
    def runRecord():
        if Record.recordState == RecordStates.Pause:
            Record.startTime += time.clock() - Record.deltaTime
            Record.deltaTime = 0
            print("Pause active")
            Record.recordState = RecordStates.Run
        else:
            Record.startTime = time.clock()
            Record.deltaTime = 0
            print("First start")
            Record.recordState = RecordStates.Stop

            if Record.recordThread is not None:
                Record.recordThread.join()

            Record.recordState = RecordStates.Run
            if Record.source is None:
                Record.recordThread = threading.Thread(target=Record.Record)
            else:
                Record.recordThread = threading.Thread(target=Record.Play)
            Record.recordThread.start()
        Record.pauseEventRunState.set()

    @staticmethod
    def stopRecord():
        Record.pauseEventRunState.set()
        Record.recordState = RecordStates.Stop

    @staticmethod
    def pauseRecord():
        Record.deltaTime = time.clock()
        Record.recordState = RecordStates.Pause
        Record.pauseEventRunState.clear()

    @staticmethod
    def getDataFromLen(startPosition, length):
        startPosition = min(startPosition, len(Record._frames))
        finishPosition = min(startPosition + length, len(Record._frames))

        if startPosition > finishPosition:
            return []
        else:
            return Record._frames[startPosition:finishPosition]

    @staticmethod
    def getDataFromTo(startPosition, finishPosition):
        startPosition = min(startPosition, len(Record._frames))
        finishPosition = min(finishPosition, len(Record._frames))

        if startPosition > finishPosition:
            return []
        else:
            return Record._frames[startPosition:finishPosition]

    @staticmethod
    def getAllDataFrom(startPosition):
        startPosition = min(startPosition, len(Record._frames))
        return Record._frames[startPosition:]

    @staticmethod
    def getCurrentId():
        return len(Record._frames)

    @staticmethod
    def Truncate(ui):
        Record._frames = []

    WAVE_OUTPUT_FILENAME = "output.wav"
    WAVE_CLEAR_OUTPUT_FILENAME = "clear_output.wav"

    @staticmethod
    def Record():
        Record.RATE = 8000
        Record.CHUNK = 512
        Record.AMPLITUDE = 2 ** 15
        FORMAT = pyaudio.paInt16
        CHANNELS = 1

        # RECORD_SECONDS = 5


        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=Record.RATE,
                        input=True,
                        frames_per_buffer=Record.CHUNK)

        print("Recording...")

        while Record.recordState != RecordStates.Stop:
            # print("In Record")
            data = stream.read(Record.CHUNK)
            Record._frames.append(data)
            Record.pauseEventRunState.wait()

        print("Done recording.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(Record.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(Record.RATE)
        wf.writeframes(b''.join(Record._frames))
        wf.close()

        wf = wave.open(Record.WAVE_CLEAR_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(Record.RATE)
        wf.writeframes(b''.join(Record._clear_frames))
        wf.close()

        Record._frames = []

        import register as reg1
        print("imp")
        for ind in reg1.Register.activeIndicators.values():
            Record.writeIndicator(ind)

    @staticmethod
    def analyse(dic, start, finish):
        start = min(start, dic.size)
        finish = min(finish, dic.size)
        sum = 0
        mx = dic[start]
        mn = dic[start]
        avg = 0
        for i in range(start, finish):
            sum += dic[i]
            mx = max(mx, dic[i])
            mn = min(mn, dic[i])
        avg = 1.0 * sum / (finish - start)
        return (sum, avg, mn, mx)

    @staticmethod
    def writeIndicator(indic):
        print(indic.getName())
        with open("logs/log_" + indic.getName() + ".txt", "w+") as f:
            perHalfOfSec = math.floor(0.5 / indic.dataTimeSpeed)
            idSec = 0
            print("sec: (sum, avg, min, max)", file=f)
            for i in range(0, indic.data.size, perHalfOfSec):
                print(str(idSec) + "s: " + str(Record.analyse(indic.data, i, i + perHalfOfSec)), file=f)
                idSec += 0.5

    @staticmethod
    def Play():
        Record.CHUNK = 512
        wf = wave.open(Record.source, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        print("Playing...")

        Record.pauseEventRunState.wait()
        while Record.recordState != RecordStates.Stop:
            data = wf.readframes(Record.CHUNK)
            stream.write(data)
            if len(data) > 0:
                Record._frames.append(data)
            else:
                Record.ui.stopButtonPress()
            Record.pauseEventRunState.wait()

        print("Done recording.")

        stream.stop_stream()
        stream.close()
        p.terminate()
        Record._frames = []
        Record.stopRecord()
