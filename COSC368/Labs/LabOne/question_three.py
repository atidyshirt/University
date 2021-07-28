from tkinter import *
from tkinter.ttk import *

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

def clear(text_out):
    text_out.set("")

root = Tk()

frame = Frame(root)
frame.pack(side='top', fill='x')
key_frame = Frame(root)
key_frame.pack(side='top', fill='x')
text_out = StringVar()
label = Label(frame, textvariable=text_out)
label.pack(side='left', fill='x')
clear_btn = Button(frame, text='clear')
clear_btn.pack(side='right', fill='x')

frame.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)

for row in range(len(board)):
    for col in range(len(board[row])):
        char = board[row][col]
        key = Button(key_frame, text=char)
        key.config(height=2, width=3)
        key.grid(row=row, col=col)

root.mainloop()

