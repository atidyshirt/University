from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import getpass
import time
import random
import operator
import itertools

class Board:
    def __init__(self, distances, widths, reps):
        self.root = Tk()
        self.start = time.time()
        self.file = open("log.log", "w")
        self.left = Bar(distances, widths, reps)
        self.right = Bar(distances, widths, reps)
        self.canvas = Canvas(self.master, width=800, height=600)
        self.canvas.pack().config(background="white")

    def log(self):
        pos = (self.a[self.index][0], self.a[self.index][1])
        self.total = (time.time() - self.start) * 1000
        self.file.write(str(getpass.getuser())+ " " + str(self.a[self.index][0]) +
                        " " + str(self.a[self.index][1])+ " " + str(self.repdict[pos]) + " "
                        + str(round(self.total, 1)) + "\n" )
        self.start = time.time()
        return


reps = 2
distances = [64, 128, 256, 212]
widths = [4, 8, 16, 32]
board = Board(distances, widths, reps)
board.root.mainloop()
