from tkinter import *
from random import *

def color_check(guessed_color):
    global display_label, color_label, chosen_color
    
    if guessed_color == chosen_color:
        display_label.config(text="Guessed right!")
        generate_color()
    else:
        display_label.config(text="Guessed wrong!")
        generate_color()
        
def generate_color():
    global chosen_color
    chosen_color = choice(["red", "green", "blue"])
    color_label.config(bg=chosen_color)

window = Tk()
window.title("Guess the color")

color_label = Label(window, bg="black", width=20)
color_label.grid(row=0, columnspan=3)

red_button = Button(window, fg="black", text="RED", command=lambda: color_check("red"))
red_button.grid(row=1, column=0)

green_button = Button(window, fg="black", text="GREEN", command=lambda: color_check("green"))
green_button.grid(row=1, column=1)

blue_button = Button(window, fg="black", text="BLUE", command=lambda: color_check("blue"))
blue_button.grid(row=1, column=2)

generate_color()

display_label = Label(window, text="Waiting")
display_label.grid(row=2, columnspan=3)

window.mainloop()

# Used ChatGPT for debugging
# Note to self
# Choice() is used to randomly select an element from a list