from tkinter import *
from tkinter.ttk import *
master = Tk()
c = Canvas(master, width=200, height=200)
c.pack()
c.create_line(0, 0, 200, 100, tag="cool")
c.create_line(0, 100, 200, 0, tag="cool", fill="red", dash=(4, 4))
rect = c.create_rectangle(50, 25, 150, 75, tag="rect", fill="red")
c.coords('rect', 10, 10, 50, 100)
c.itemconfigure('cool', fill='red')
c.itemconfigure(rect, fill='red')

master.mainloop()
