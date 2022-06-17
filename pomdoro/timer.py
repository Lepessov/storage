import time

from tkinter import *

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class Timer:

    def __init__(self):
        self.seconds = 0 
        self.work_min = WORK_MIN

    def start(self):
        if self.seconds == 0:
            self.work_min -= 1
            self.seconds = 59 
        else:
            self.seconds -= 1

        return f'{self.work_min}:{self.seconds}'

    def break_time(self, minutes):
        self.work_min = minutes
        self.seconds = 0

    def reset(self):
        self.seconds = 0
        self.work_min = WORK_MIN

