from tkinter import Tk, Label, Button, Frame
from pyautogui import *
from threading import Thread
from time import sleep

record = False
recorded_positions = []

def recording():
    while record:
        x, y = position()
        recorded_positions.append([x,y])
        sleep(0.1)

def start_record():
    global record
    record = True
    Thread(target=recording).start()
    start_rec_btn.config(state="disabled")
    stop_rec_btn.config(state="active")
    status_label.config(text="Recording started!")

def stop_record():
    global record
    record = False
    stop_rec_btn.config(state="disabled")
    play_rec_btn.config(state="active")
    clear_rec_btn.config(state="active")
    status_label.config(text="Recording stopped!")

def play_record():
    status_label.config(text="Playing recording!")
    for position in recorded_positions:
        moveTo(int(position[0]), int(position[1]), 0.1)
    status_label.config(text="Finished playing recording!")

def clear_record():
    global recorded_positions
    recorded_positions = []
    start_rec_btn.config(state="active")
    stop_rec_btn.config(state="disabled")
    play_rec_btn.config(state="disabled")
    clear_rec_btn.config(state="disabled")
    status_label.config(text="Cleared recording!")

window = Tk()
window.title("Mouse movement recorder")

frame_one = Frame(window)

start_rec_btn = Button(frame_one, text="Start", width=10, height=6, command=lambda: start_record())
start_rec_btn.grid(row=0, column=0)

stop_rec_btn = Button(frame_one, text="Stop", width=10, height=6, state="disabled", command=lambda: stop_record())
stop_rec_btn.grid(row=0, column=1)

play_rec_btn = Button(frame_one, text="Play", width=10, height=6, state="disabled", command=lambda: play_record())
play_rec_btn.grid(row=0, column=2)

clear_rec_btn = Button(frame_one, text="Clear", width=10, height=6, state="disabled", command= lambda: clear_record())
clear_rec_btn.grid(row=0, column=3)

frame_one.grid(row=0, column=0)

status_label = Label(window, text="Waiting for information", height=3)
status_label.grid(row=1, column=0)

window.mainloop()
