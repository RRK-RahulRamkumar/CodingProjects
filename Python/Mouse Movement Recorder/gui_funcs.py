from threading import Thread
from pyautogui import *
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

def stop_record():
    global record
    record = False

def play_record():
    for position in recorded_positions:
        moveTo(int(position[0]), int(position[1]), 0.1)

def clear_record():
    global recorded_positions
    recorded_positions = []

def main(func_code):
    
    if func_code == 1:
       start_record()
    elif func_code == 2:
        stop_record()
    elif func_code == 3:
        play_record()
    elif func_code == 4:
        clear_record()
