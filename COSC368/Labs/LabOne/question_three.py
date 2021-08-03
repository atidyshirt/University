from tkinter import *


def do_nothing():
    print("do nothing")

window = Tk()
fullFrame = Frame(window, height=50, width=350, borderwidth=4)
fullFrame.pack()

display = Frame(fullFrame, height=50, width=350)
display.pack_propagate(0)
display.pack()
txtDisplay = Entry(display, bd=2, width=28, font = 30) #bd is border
txtDisplay.pack(side=LEFT, fill=X)
clear = Button(display, text="Clear")
clear.pack(side=RIGHT)

keyboard = Frame(fullFrame, borderwidth=2, relief=RAISED)
keyboard.pack(side=BOTTOM)

row1 = Frame(keyboard)
row2 = Frame(keyboard)
row3 = Frame(keyboard)

row1.pack()
row2.pack()
row3.pack()


board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
row = [row1,row2,row3]
rowIndex = 0
for line in board:
    for letter in line:
        button = Button(row[rowIndex], text=letter)
        button.pack(side=LEFT)
    rowIndex += 1

window.mainloop()
