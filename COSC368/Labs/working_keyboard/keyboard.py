"""
This version of the working keyboard was given to me
by Fletcher Dick (Fellow course mate) as mine was not
fully functional from lab two.
"""

import time
from tkinter import *
import random
import string
import csv


class keyboard:

    def __init__(self):
        self.isStatic = False
        self.name = "Jordan"
        self.goal = 6
        self.iter = 0
        self.block_count = 6
        self.start = time.time()

        # Create block and current block
        self.alpha = list(string.ascii_lowercase)
        random.shuffle(self.alpha)
        self.block = self.alpha[:6]
        self.cur_block = self.block[:]
        print(f"Block: {self.block} at round {self.iter + 1} of {self.goal}")

        # Initiate random keyboard pattern

        window = Tk()
        # Set the first target from block
        self.output_text = StringVar()
        self.set_target()

        # Set up UI
        output_frame = Frame(window)
        output_frame.pack(side="top", fill="x", padx=5, pady=5)

        label = Label(output_frame, textvariable=self.output_text)
        label.pack(side='left', fill='x')

        output_frame.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=2)

        self.input_frame = Frame(window, relief=RIDGE)
        self.shuffle_keyboard()

        window.mainloop()

    def set_target(self):
        self.output_text.set(self.cur_block.pop(random.randrange(0, len(self.cur_block))))

    def end(self):
        self.input_frame.destroy()
        self.output_text.set('Finished')

    def log(self, char):
        total_time = (time.time() - self.start) * 1000
        print(f"{self.name} {'static' if self.isStatic else 'dynamic'} {char} {self.block_count} {total_time:.1f}")

        csv_file_name = 'experiment_static_log.txt' if self.isStatic else 'experiment_dynamic_log.txt'
        with open(csv_file_name, 'a', newline='') as csvfile:
            self.file_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            self.file_writer.writerow(
                [self.name, 'static' if self.isStatic else 'dynamic', char, self.block_count, f"{total_time:.1f}"])
        self.start = time.time()
        self.block_count = 1

    def reshuffle_block(self):
        random.shuffle(self.block)
        self.cur_block = self.block[:]

    def shuffle_keyboard(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        random.shuffle(self.alpha)
        board = [self.alpha[:10],
            self.alpha[10:19],
            self.alpha[19:]]

        self.input_frame.pack(side="bottom", fill="x", padx=5, pady=5)

        for row in range(len(board)):
            for col in range(len(board[row])):
                ch = board[row][col]

                key_frame = Frame(self.input_frame, height=32, width=32)
                key_frame.pack_propagate(0)  # don't shrink
                key_frame.grid(row=row, column=col * 2 + row, columnspan=2)
                key = Button(key_frame, text=ch, command=lambda x=ch: self.check_correct(x))
                key.pack(fill=BOTH, expand=1)

    def check_correct(self, char):
        if char == self.output_text.get():
            self.log(char)
            if not self.isStatic:
                self.shuffle_keyboard()
            if len(self.cur_block) != 0:
                self.set_target()
            else:  # End of current block chars
                self.iter += 1
                if self.iter == self.goal:  # Finished
                    self.end()
                else:
                    self.reshuffle_block()
                    print(f"Block: {self.block} at round {self.iter + 1} of {self.goal}")
                    self.set_target()
        else:
            self.block_count += 1


keyboard()
