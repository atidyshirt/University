from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import getpass
import time
import random
import operator
import itertools

class fitts(object):
    def __init__(self, distances, widths, reps):
        self.index = 0
        self.reps = reps
        self.distances = distances
        self.widths = widths
        self.distances = random.sample(self.distances, len(self.distances))
        self.widths = random.sample(self.widths, len(self.distances))

        self.a = list(itertools.product( self.distances,self.widths))

        self.master = Tk()
        self.file = open("experiment_fitts_log.txt","w")

        self.green = "left"
        self.repdict = {}

        self.start = time.time()
        self.setup()

    def setup(self):
        self.c = Canvas(self.master, width=800, height=600)
        self.c.pack()
        self.c.config(background="white")
        leftbottom, lefttop, rightbottom, righttop = self.positions()
        leftRect = self.c.create_rectangle(leftbottom, 0, lefttop, 600,
                                    tag="left", fill="green", outline="green")
        rightRect = self.c.create_rectangle(rightbottom, 0, righttop, 600,
                                    tag="right", fill="blue", outline="blue")

        self.c.tag_bind("left", "<ButtonPress-1>", self.leftClick)
        self.c.tag_bind("right", "<ButtonPress-1>",  self.rightClick)

    def leftClick(self, dummy):
        if self.green == "left":

            leftbottom, lefttop, rightbottom, righttop = self.positions()

            self.c.itemconfigure("left", fill="blue", outline="blue")
            self.c.itemconfigure("right", fill="green", outline="green")
            self.c.coords("left", leftbottom, 0, lefttop, 600)
            self.c.coords("right", rightbottom, 0, righttop, 600)
            self.green = "right"

            return
        else:
            return

    def rightClick(self, dummy):
        if self.green == "right":

            leftbottom, lefttop, rightbottom, righttop = self.positions()

            self.c.itemconfigure("right", fill="blue", outline="blue")
            self.c.itemconfigure("left", fill="green", outline="green")
            self.c.coords("right", rightbottom, 0, righttop, 600)
            self.c.coords("left", leftbottom, 0, lefttop, 600)
            self.green = "left"

            return
        else:
            return

    def positions(self):
        pos = (self.a[self.index][0], self.a[self.index][1])
        if pos in self.repdict:
            if self.repdict[pos] == (self.reps - 1):
                self.index += 1
                if self.index == len(self.a):
                    self.file.close()
                    popup = messagebox.showinfo('Thank You','You have completed the test')
                    self.master.destroy()
                    return popup
                pos = (self.a[self.index][0], self.a[self.index][1])
                self.repdict[pos] = 0
                self.log()
            else:
                self.repdict[pos] += 1

                self.log()
        else:
            self.repdict[pos] = 0

            self.log()

        center = 400
        leftbottom = center - self.a[self.index][0]
        rightbottom = center + self.a[self.index][0]
        lefttop = (center - self.a[self.index][0]) - self.a[self.index][1]
        righttop = (center + self.a[self.index][0]) + self.a[self.index][1]
        return leftbottom, lefttop, rightbottom, righttop

    def log(self):
        pos = (self.a[self.index][0], self.a[self.index][1])
        self.total = (time.time() - self.start) * 1000
        self.file.write(str(getpass.getuser())+ " " + str(self.a[self.index][0]) +
                        " " + str(self.a[self.index][1])+ " " + str(self.repdict[pos]) + " "
                        + str(round(self.total, 1)) + "\n" )
        self.start = time.time()
        return

if __name__ == "__main__":
    reps = 2
    distances = [64, 128, 256, 212]
    widths = [4, 8, 16, 32]
    go = fitts(distances, widths, reps)
    go.master.mainloop()
