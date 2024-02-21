from tkinter import Tk, Label, Button, font

original_dimension = 5

yes_dimension = original_dimension
no_dimension = original_dimension
no_button_delay = 3000
yes_button_delay = 5000
text_label_delay = 7000

font_size_increment = 5
yes_dimension_increment = 5
no_dimension_increment = 5
yes_count = 0

text_list = ["Excited?", "Smiling?"]
text_list_index = 0

def no_function():
    global yes_dimension
    yes_dimension += yes_dimension_increment
    yes_button.config(width=yes_dimension, height=yes_dimension)

def yes_function():
    global yes_count, no_dimension, yes_dimension, custom_font, font_size, text_list_index
    yes_count += 1
    no_dimension += 5

    if yes_count <= len(text_list):
        font_size += no_dimension_increment
        text_label.config(text=text_list[text_list_index], font=custom_font)
        text_list_index += 1
        custom_font.config(size=font_size)
        no_button.config(width=no_dimension, height=no_dimension)
    else:
        yes_button.config(state="disabled")
        no_button.config(state="disabled")
        font_size += no_dimension_increment
        text_label.config(text="Have a great day!", font=custom_font)
        no_button.config(width=no_dimension, height=no_dimension)

        yes_dimension = original_dimension
        no_dimension = original_dimension
        yes_count = 0
        text_list_index = 0

        no_button.after(no_button_delay, lambda: no_button.config(width=no_dimension, height=no_dimension))
        yes_button.after(yes_button_delay, lambda: yes_button.config(width=yes_dimension, height=yes_dimension))
        font_size = original_font_size
        custom_font.config(size=font_size)
        text_label.after(text_label_delay, lambda: text_label.config(text="Are you happy?", font=custom_font))

        yes_button.after(text_label_delay, lambda: yes_button.config(state="active", activebackground="white"))
        no_button.after(text_label_delay, lambda: no_button.config(state="active", activebackground="white"))

window = Tk()

original_font_size = 15
font_size = original_font_size
custom_font = font.Font(family="Arial", size=font_size)

window.title("Fun GUI")
window.resizable(False, False)

text_label = Label(window, text="Are you happy?", height=5, font=custom_font)
text_label.grid(row=0, columnspan=3)

yes_button = Button(window, text="Yes", width=yes_dimension, height=yes_dimension, activebackground="white", command=yes_function)
yes_button.grid(row=1, column=1)

no_button = Button(window, text="No", width=no_dimension, height=no_dimension, activebackground="white", command=no_function)
no_button.grid(row=1, column=2)

window.mainloop()

# Used ChatGPT for debugging