from tkinter import *

set_username = "testing"
set_password = "3411"

def verify(set_username, set_password):
    global username, password, error_label
    entered_username = username.get()
    entered_password = password.get()

    if set_username == entered_username and set_password == entered_password:
        error_label.config(text="Login successful")
    else:
        error_label.config(text="Invalid credentials")
        username.delete(0, END)
        password.delete(0, END)


window = Tk()
window.title("Simple Login V1")

label1 = Label(window, text="Username:")
label1.grid(row=0, column=0)
username = Entry(window, bg="light grey", fg="black")
username.grid(row=0, column=1)

label2 = Label(window, text="Password:")
label2.grid(row=1, column=0)
password = Entry(window, bg="light grey", fg="black")
password.grid(row=1, column=1)

error_label = Label(window, text="...")
error_label.grid(row=2, columnspan=2)
submit = Button(window, text="Login in", command= lambda: verify(set_username, set_password))
submit.grid(row=4, columnspan=2)

window.mainloop()