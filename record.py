import pyaudio
import wave
import threading
import matplotlib.pyplot as plt
import numpy
from details_classes import *


class Record:
    # сам тред записи
    recordThread = None
    # текущее состояние треда
    recordState = RecordStates.Stop
    # флаг НЕ активности паузы
    pauseEventRunState = threading.Event()
    # записываемые данные
    _frames = []
    RATE = 44100
    CHUNK = 1024
    AMPLITUDE = 2 ** 15

    @staticmethod
    def runRecord():

        if Record.recordState == RecordStates.Pause:
            print("Pause active")
            Record.recordState = RecordStates.Run
        else:
            print("First start")
            Record.recordState = RecordStates.Stop

            if Record.recordThread is not None:
                Record.recordThread.join()

            Record.recordState = RecordStates.Run
            Record.recordThread = threading.Thread(target=Record.Record)
            Record.recordThread.start()
        Record.pauseEventRunState.set()

    @staticmethod
    def stopRecord():
        Record.pauseEventRunState.set()
        Record.recordState = RecordStates.Stop

    @staticmethod
    def pauseRecord():
        Record.recordState = RecordStates.Pause
        Record.pauseEventRunState.clear()

    @staticmethod
    def getDataFromLen(startPosition, length):
        startPosition = min(startPosition, len(Record._frames))
        finishPosition = min(startPosition + length, len(Record._frames))
        return Record._frames[startPosition:finishPosition]

    @staticmethod
    def getDataFromTo(startPosition, finishPosition):
        startPosition = min(startPosition, len(Record._frames))
        finishPosition = min(finishPosition, len(Record._frames))
        return Record._frames[startPosition:finishPosition]

    @staticmethod
    def getAllDataFrom(startPosition):
        startPosition = min(startPosition, len(Record._frames))
        return Record._frames[startPosition:]

    @staticmethod
    def getCurrentId():
        return len(Record._frames)

    @staticmethod
    def Record():
        FORMAT = pyaudio.paInt16
        CHANNELS = 1

        # RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "output.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=Record.RATE,
                        input=True,
                        frames_per_buffer=Record.CHUNK)

        print("Recording...")

        while Record.recordState != RecordStates.Stop:
            print("In Record")
            data = stream.read(Record.CHUNK)
            Record._frames.append(data)
            Record.pauseEventRunState.wait()

        print("Done recording.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(Record.RATE)
        wf.writeframes(b''.join(Record._frames))
        wf.close()

        frames = b''.join(Record._frames)

        fig = plt.figure()
        s = fig.add_subplot(111)
        amplitude = numpy.fromstring(frames, numpy.int16)
        s.plot(amplitude)
        fig.savefig('t.png')
