import time
import math

from tkinter import *

from timer import Timer

WORK_MIN = 1 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

timer = Timer()
window = Tk()
window.title('Pomdoro App')
window.config(padx=110, pady=50, bg='#f7f5dd')

lable = Label(text='Timer', font=('Courier', 35, 'bold'), bg='#f7f5dd', fg='#9bdeac')
lable.grid(column=1, row=0)

def reset_timer():
    start_timer()

def start_timer():

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec, 'green')
    elif reps == 8:
        count_down(long_break_sec, 'black')
    else:
        count_down(short_break_sec, 'blue')

def count_down(seconds, color):

    minutes = math.floor(seconds / 60)
    sec = seconds % 60

    if int(sec) < 10:
        sec = f'0{sec}'

    canvas.itemconfig(canva_text, text=f'{minutes}:{sec}', fill=f'{color}')

    if seconds > 0:
        window.after(1000, count_down, seconds - 1, f'{color}')
    else:
        start_timer()

canvas = Canvas(width=250, height=224, bg='#f7f5dd', highlightthickness=0)
tomat_img = PhotoImage(file='images.png')
canvas.create_image(119, 112, image=tomat_img)

canva_text = canvas.create_text(119, 112, text='00:00', fill='white', font=('Courier', 35, 'bold'))
canvas.grid(column=1, row=1)

reset = Button(text='Reset', command=reset_timer)
reset.grid(column=2, row=2)

start = Button(text='Start', command=start_timer) 
start.grid(column=0, row=2)


window.mainloop()
