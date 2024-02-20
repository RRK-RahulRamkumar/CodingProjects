# This code is written to understand the basics of sockets
# --------------------------------
# ------- Server side code -------
# --------------------------------

from socket import *
from tkinter import Tk, Label, Entry, Button
from threading import Thread

def connection(server_ip, server_port, queue_limit, buffer_size, data_to_share):
    log_texts = ""

    # Creating a socket using the with statement
    with socket(AF_INET, SOCK_STREAM) as server_socket:
        
        # Assigns the socket to an ip address and a port
        server_socket.bind((server_ip, server_port))

        # Enables the socket to receive connections upto the queue limit
        server_socket.listen(queue_limit)

        # Accept the received connection, which returns a tuple with client socket and client address
        client_socket, client_address = server_socket.accept()
        log_texts += f"Connection established with {client_address}.\n"

        # To receive data from the client socket, decoding it using .decode()
        received_data = client_socket.recv(buffer_size).decode()
        received_data_label.config(text=f"{received_data}")

        log_texts += f"Client shared the data.\n"

        # To send data to the client
        client_socket.sendall(bytes(data_to_share, 'utf-8'))
        log_texts += "Shared data with client.\n"

        # To end the connection between the server and the client socket
        client_socket.close()
        log_texts += f"Connection with {client_address} closed."

    
    log.config(text=log_texts)

def start_server():

    server_ip = ip_entry.get()
    server_port = int(port_entry.get())
    queue_limit = int(Q_limit_entry.get())
    buffer_size = int(buffer_entry.get())
    data_to_share = data_entry.get()

    received_data_label.config(text="No data received.")
    log.config(text="No data to log.")

    Thread(target=connection, args=(server_ip, server_port, queue_limit, buffer_size, data_to_share)).start()

window = Tk()
window.title("Server configuration")
window.resizable(False, False)

received_data_label = Label(window, text="Server inactive.", width=50, height=10, bg="light grey", fg="black")
received_data_label.grid(row=0, column=0)

log = Label(window, text="Server inactive.", width=50, height=10, bg="grey", fg="black")
log.grid(row=1, column=0)

empty_label1 = Label(window, width=50)
empty_label1.grid(row=2, column=0)

text_label1 = Label(window, text="Server IP:")
text_label1.grid(row=3, columnspan=1, sticky="w")
ip_entry = Entry(window, width=30)
ip_entry.grid(row=3, column=0)


text_label2 = Label(window, text="Server Port:")
text_label2.grid(row=4, columnspan=1, sticky="w")
port_entry = Entry(window, width=30)
port_entry.grid(row=4, column=0)

text_label3 = Label(window, text="Queue Limit:")
text_label3.grid(row=5, columnspan=1, sticky="w")
Q_limit_entry = Entry(window, width=30)
Q_limit_entry.grid(row=5, column=0)

text_label4 = Label(window, text="Buffer Size:")
text_label4.grid(row=6, columnspan=1, sticky="w")
buffer_entry = Entry(window, width=30)
buffer_entry.grid(row=6, column=0)

text_label5 = Label(window, text="Data to share:")
text_label5.grid(row=7, columnspan=1, sticky="w")
data_entry = Entry(window, width=30)
data_entry.grid(row=7, column=0)

empty_label2 = Label(window, width=50)
empty_label2.grid(row=8, column=0)

start_server_button = Button(window, text="Start Server", command=start_server)
start_server_button.grid(row=9, columnspan=1)


window.mainloop()

# Used ChatGPT for debugging and threading

# Default settings
# server_ip = '127.0.0.1' This is a loopback address, it refers to the local host
# server_port = 1234
# buffer_size = 1024


# Notes to self,
# Threading allows for the execution of multiple tasks concurrently within a single process (an instance of a program)
# For threading, targert=function name, args=(arguments for the function). args paremeter only applies if there are arguments for the function

# b"" is used to convert characters within the qoutation into bytes, you can use "".encode() or bytes("", "type of encoding, generally utf-8")

# send(data) Sends the specified data over the socket. It will attempt to send as much data as possible in a single call, up to the buffer size. 
#   If the buffer is full and not all data is sent, 
#   the unsent data remains in the buffer and must be sent manually by calling send() again.
# sendall(data): Sends all the data in the buffer over the socket. 
#   It repeatedly calls send() to send all the data until either all data has been sent or an error occurs. 
#   It ensures that all data is sent before returning, simplifying the process of sending large amounts of data.

# The server socket is used only for accepting connections.
# Once a connection is accepted, both the server and the client use the same client socket to communicate over the established connection.

# Functions can always access global variables but cannot modify them unless the global keyword is used

# AF_INET refers to IPV4, SOCK_STREAM refers to TCP

# --------------------------------
# ------- Client side code -------
# --------------------------------
from socket import *
from tkinter import Tk, Label, Entry, Button
from threading import Thread

def connection(server_ip, server_port, buffer_size, data_to_share):
    log_texts = ""

    # Creating a socket using the with statement
    with socket(AF_INET, SOCK_STREAM) as client_socket:

        # Connecting the server socket
        client_socket.connect((server_ip, server_port))
        log_texts += f"Connection established with {server_ip}.\n"

        # Sending data to the server using the client socket
        client_socket.sendall(bytes(data_to_share, "utf-8"))
        log_texts += f"Data shared with server.\n"

        # Receving data from the server using the client socket
        received_data = client_socket.recv(buffer_size).decode()
        log_texts += f"Data received from server.\n"
        received_data_label.config(text=f"{received_data}")

        log_texts += f"Connection with {server_ip} closed.\n"

    log.config(text=log_texts)

def connect_client():

    server_ip = ip_entry.get()
    server_port = int(port_entry.get())
    buffer_size = int(buffer_entry.get())
    data_to_share = data_entry.get()

    received_data_label.config(text="No data received.")
    log.config(text="No data to log.")

    Thread(target=connection, args=(server_ip, server_port, buffer_size, data_to_share)).start()

window = Tk()
window.title("Client configuration")
window.resizable(False, False)


received_data_label = Label(window, text="Client inactive.", width=50, height=10, bg="light grey", fg="black")
received_data_label.grid(row=0, column=0)

log = Label(window, text="Client inactive.", width=50, height=10, bg="grey", fg="black")
log.grid(row=1, column=0)

empty_label1 = Label(window, width=50)
empty_label1.grid(row=2, column=0)

text_label1 = Label(window, text="Server IP:")
text_label1.grid(row=3, columnspan=1, sticky="w")
ip_entry = Entry(window, width=30)
ip_entry.grid(row=3, column=0)


text_label2 = Label(window, text="Server Port:")
text_label2.grid(row=4, columnspan=1, sticky="w")
port_entry = Entry(window, width=30)
port_entry.grid(row=4, column=0)

text_label3 = Label(window, text="Buffer Size:")
text_label3.grid(row=5, columnspan=1, sticky="w")
buffer_entry = Entry(window, width=30)
buffer_entry.grid(row=5, column=0)

text_label4 = Label(window, text="Data to share:")
text_label4.grid(row=6, columnspan=1, sticky="w")
data_entry = Entry(window, width=30)
data_entry.grid(row=6, column=0)

empty_label2 = Label(window, width=50)
empty_label2.grid(row=7, column=0)

connect_client_button = Button(window, text="Connect client", command=connect_client)
connect_client_button.grid(row=8, columnspan=1)


window.mainloop()

# Client side code must be run on another terminal