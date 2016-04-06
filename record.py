import pyaudio
import wave
import threading
import matplotlib.pyplot as plt
import numpy
from details_classes import *

# сам тред записи
recordThread = None
# текущее состояние треда
recordState = RecordStates.Stop
# флаг НЕ активности паузы
pauseEventRunState = threading.Event()


def runRecord():
    global recordState, recordThread, pauseEventRunState

    if recordState == RecordStates.Pause:
        print("Pause active")
        recordState = RecordStates.Run
    else:
        print("First start")
        recordState = RecordStates.Stop

        if recordThread is not None:
            recordThread.join()

        recordState = RecordStates.Run
        recordThread = threading.Thread(target=Record)
        recordThread.start()
    pauseEventRunState.set()


def stopRecord():
    global recordState, pauseEventRunState
    pauseEventRunState.set()
    recordState = RecordStates.Stop


def pauseRecord():
    global recordState, pauseEventRunState
    recordState = RecordStates.Pause
    pauseEventRunState.clear()


def Record():
    global recordState, pauseEventRunState
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    while recordState != RecordStates.Stop:
        print("In Record")
        data = stream.read(CHUNK)
        #print(data)
        frames.append(data)
        pauseEventRunState.wait()

    print("Done recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    fig = plt.figure()
    s = fig.add_subplot(111)
    amplitude = numpy.fromstring(frames, numpy.int16)
    s.plot(amplitude)
    fig.savefig('t.png')
