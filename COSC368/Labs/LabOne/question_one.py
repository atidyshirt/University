from tkinter import *
from tkinter.ttk import *

def clear_data(data):
    data.set("")

window = Tk()
data = StringVar()
data.set("Data to display")
label = Label(window, textvariable=data)
label.grid(row=0, column=0)
entry = Entry(window, textvariable=data)
entry.grid(row=1, column=0)
clear = Button(window, text="Clear", command=lambda: clear_data(data))
clear.grid(row=2, column=0)
quit = Button(window, text="Quit", command=window.destroy)
quit.grid(row=3, column=0)
window.mainloop()
