import subprocess

class Pypkr:
    def __init__(self):
        self.language = "en"
        self.voices = "m3"
        self.speed = 175
        self.volume = 100
        self.word_gap = 0
        self.pitch = 50
        self.espeak = 0
        self.__version__ = "2.0.3"
        self.__list_espeak__ = ["espeak", "espeak-ng"]
        self.name = "a.wav"

    def __if__(self):
        if int(self.speed) < 1:
            self.speed = 175
        if int(self.volume) < 1:
            self.volume = 100
        if int(self.pitch) < 1:
            self.pitch = 50
        if int(self.word_gap) < 0:
            self.word_gap = 0
        if int(self.espeak) != 0 and int(self.espeak) != 1:
            self.espeak = 0

    def voice(self, data, data1):
        if data == 'm':
            if data1 < 8 and data1 > 0:
                    self.voices = 'm' + str(data1)
                    return 0
            else:
                return 1
        elif data == 'f':
            if data1 < 5 and data1 > 0:
                self.voices = 'f' + str(data1)
                return 0
            else:
                return 1
        else:
            return 1

    def say(self, data):
        self.__if__()

        subprocess.run([
            self.__list_espeak__[int(self.espeak)],
            "-v", str(self.language)+'+'+str(self.voices),
            "-s", str(self.speed),
            "-a", str(self.volume),
            "-g", str(self.word_gap),
            "-p", str(self.pitch),
            data
        ])
    def save_to_file(self, data):
        self.__if__()

        subprocess.run([
            self.__list_espeak__[int(self.espeak)],
            "-v", str(self.language)+'+'+str(self.voices),
            "-s", str(self.speed),
            "-a", str(self.volume),
            "-g", str(self.word_gap),
            "-p", str(self.pitch),
            data, "-w",
            str(self.name)
        ])
