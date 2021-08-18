from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import getpass
import time
import math
import random
import operator
import itertools
import sys

CENTER = 400

class Board:
    def __init__(self, distances, widths, reps):
        # Inputs
        self.distances = random.sample(distances, len(distances))
        self.widths = random.sample(widths, len(distances))
        # How many
        self.index = 0
        self.reps = reps
        self.stored = {}
        # Iterations
        self.dist_x_width = list(
            itertools.product(self.distances, self.widths))
        # Window
        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        # Timer
        self.start = time.time()
        # Log file
        self.log_file = open("log.log", "w")
        # Bars
        self.pos = self.iterate_position_tuples()
        self.left = Bar(self, self.canvas, self.pos, "left", "green")
        self.right = Bar(self, self.canvas, self.pos, "right", "blue")
        self.canvas.tag_bind("left", "<ButtonPress-1>",  self.left.click)
        self.canvas.tag_bind("right", "<ButtonPress-1>",  self.right.click)

    def iterate_position_tuples(self):
        pos = (self.dist_x_width[self.index][0],
               self.dist_x_width[self.index][1])
        if pos in self.stored:
            if self.stored[pos] == (self.reps - 1):
                self.index += 1
                if self.index == len(self.dist_x_width):
                    self.log_file.close()
                    sys.exit("You have finished the test")
                pos = (self.dist_x_width[self.index][0],
                       self.dist_x_width[self.index][1])
                self.stored[pos] = 0
                self.log()
            else:
                self.stored[pos] += 1
                self.log()
        else:
            self.stored[pos] = 0
            self.log()

        return {
            "tl": (CENTER - self.dist_x_width[self.index][0]) - self.dist_x_width[self.index][1],
            "bl": (CENTER - self.dist_x_width[self.index][0]),
            "tr": (CENTER + self.dist_x_width[self.index][0]) - self.dist_x_width[self.index][1],
            "br": (CENTER + self.dist_x_width[self.index][0])
        }

    def log(self):
        pos = (self.dist_x_width[self.index][0],
               self.dist_x_width[self.index][1])
        self.total = (time.time() - self.start) * 1000
        self.log_file.write(str(self.dist_x_width[self.index][0])
            + "\t" + str(self.dist_x_width[self.index][1])
            + "\t" + str(math.log2((self.dist_x_width[self.index][0] - self.dist_x_width[self.index][1]) + 1))
            + "\t" + str(round(self.total, 1)) + "\n")
        self.start = time.time()

class Bar:
    """ Green bar acts as a controller for both bars """

    def __init__(self, board, canvas, position, tag, color):
        self.canvas = canvas
        self.board = board
        self.tag = tag
        self.color = color
        if tag == "right":
            self.visual_bar = self.canvas.create_rectangle(position['bl'], 0, position['tl'], 600,
                                                           tag=tag, fill=color, outline=color)
        else:
            self.visual_bar = self.canvas.create_rectangle(position['br'], 0, position['tr'], 600,
                                                           tag=tag, fill=color, outline=color)

    def click(self, event):
        if self.tag == "left" and self.color == "green":
            position = self.board.iterate_position_tuples()
            self.canvas.itemconfigure("left", fill="blue", outline="blue")
            self.canvas.coords("left", position['bl'], 0, position['tl'], 600)
            self.canvas.itemconfigure("right", fill="green", outline="green")
            self.canvas.coords("right", position['br'], 0, position['tr'], 600)
            self.tag = "left"
            self.color = "blue"
            self.board.right.tag = "right"
            self.board.right.color = "green"
        elif self.tag == "right" and self.color == "green":
            position = self.board.iterate_position_tuples()
            self.canvas.itemconfigure("left", fill="green", outline="green")
            self.canvas.coords("left", position['bl'], 0, position['tl'], 600)
            self.canvas.itemconfigure("right", fill="blue", outline="blue")
            self.canvas.coords("right", position['br'], 0, position['tr'], 600)
            self.tag = "right"
            self.color = "blue"
            self.board.left.tag = "left"
            self.board.left.color = "green"


reps = 2
distances = [64, 128, 256]
widths = [8, 16, 32]
board = Board(distances, widths, reps)
board.root.mainloop()
