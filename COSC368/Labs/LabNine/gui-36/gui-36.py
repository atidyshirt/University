from tkinter import *
from tkinter.ttk import *
import time
import random
import glob

icon_files = glob.glob('./icons/*.gif')

DESIGN = "thirtysix"

if DESIGN=="four":
    ROWS = 2
    COLS = 2
elif DESIGN=="nine":
    ROWS = 3
    COLS = 3
else:
    DESIGN = "thirtysix"
    ROWS = 6
    COLS = 6

showing_items = [None]*ROWS*COLS
USER_CODE = "jpy19"
TOTAL_WIDTH = 320
TOTAL_HEIGHT = 320
GESTURE_LENGTH = 50
NUM_DISTINCT_TARGETS = 5
NUM_BLOCKS = 10
page = 0
count = -1
down_x = NONE
log_file = open('experiment_%s.txt' % DESIGN, 'w')

def store_down(e):
    global down_x
    down_x = e.x

def next_target():
    global page, all_targets, current_target, count, cue
    page = 0
    show_photos(page)
    if count >= 0:
        all_targets.pop()
    if len(all_targets) == 0:
        cue.destroy()
        cue = Label(window, borderwidth=4, relief=RAISED, text="FINISHED!")
        cue.pack(side='top')
        log_file.close()
        current_target = None
    else:
        current_target = all_targets[-1]
        show_target(current_target)
        count +=1

def hit():
    global  start_time
    total_time = time.time() - start_time
    if count >= 0:
        log_file.write('%s\t%s\t%s\t%d\t%.2f\n' % \
                    (USER_CODE, DESIGN, current_target, count/NUM_DISTINCT_TARGETS, total_time))
    next_target()
    start_time = time.time()

def release(e, item):
    global down_x, page
    if e.x - down_x > GESTURE_LENGTH:
        page = (page+1) % (len(icon_files)//(ROWS*COLS))
        show_photos(page)
    elif down_x - e.x > GESTURE_LENGTH:
        page = (page-1) % (len(icon_files)//(ROWS*COLS))
        show_photos(page)
    elif icon_files[showing_items[item]] == current_target:
        hit()



def make_grid (f):
    buttons = []
    for r in range(ROWS):
        for c in range(COLS):
            b = Button(f)
            b.bind("<ButtonPress-1>", store_down)
            b.bind("<ButtonRelease-1>", lambda e, x=r*COLS+c: release(e, x))
            buttons.append(b)
            b.grid(row=r, column=c, ipady=10)
    return buttons

def make_photos():
    photos = []
    for i in range(len(icon_files)):
        p = PhotoImage(file=icon_files[i])
        photos.append(p)
    return photos

def show_photos(page):
    global buttons, showing_items
    start_index = page*ROWS*COLS
    for i in range(ROWS*COLS):
        item = start_index+i
        if item < len(icon_files):
            buttons[i].configure(image=photos[item])
            showing_items[i] = item

def make_targets():
    full_targets = icon_files[1:]
    random.shuffle(full_targets)
    target_set = full_targets[0:NUM_DISTINCT_TARGETS]
    all_targets = []
    for i in range(NUM_BLOCKS):
        random.shuffle(target_set)
        all_targets = all_targets + target_set
    return all_targets

def show_target(item):
    global p
    p = PhotoImage(file=item)
    cue.configure(image=p)


window = Tk()
window.resizable(0,0)
current_target = icon_files[0]
cue = Label(window, borderwidth=4, relief=RAISED)
show_target(current_target)
cue.pack(side='top')
fr = Frame(window, width=TOTAL_WIDTH, height=TOTAL_HEIGHT)
fr.pack(side='bottom')
buttons = make_grid(fr)
photos = make_photos()
all_targets = make_targets()
show_photos(page)
start_time = time.time()
window.mainloop()
