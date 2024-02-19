# This code is written to understand the basics of sockets
# ------- Server side code -------

from socket import *
from tkinter import Tk, Label
from threading import Thread

server_ip = '127.0.0.1'
server_port = 1234
queue_limit = 1
buffer_size = 1024
data_to_share = b''

def connection(server_ip, server_port, queue_limit, buffer_size, data_to_share):
    log_texts = ""
    received_data = ""

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
        received_data_label.config(text=f"Client shared the data: {received_data}.")

        log_texts += f"Client shared the data.\n"

        # To send data to the client
        client_socket.sendall(data_to_share)
        log_texts += "Shared data with client.\n"

        # To end the connection between the server and the client socket
        client_socket.close()
        log_texts += f"Connection with {client_address} closed."

    
    log.config(text=log_texts)


window = Tk()


received_data_label = Label(window, text="No data received.", width=50, height=10, bg="light grey", fg="black")
received_data_label.grid(row=0, column=0)

log = Label(window, text="Nothing to log.", width=50, height=10, bg="grey", fg="black")
log.grid(row=1, column=0)


Thread(target=connection, args=(server_ip, server_port, queue_limit, buffer_size, data_to_share)).start()


window.mainloop()

# Used ChatGPT for debugging and threading
#
# Notes to self,
# Threading allows for the execution of multiple tasks concurrently within a single process (an instance of a program)
# For threading, targert=function name, args=(arguments for the function). args paremeter only applies if there are arguments for the function
#
# b"" is used to convert characters within the qoutation into bytes, you can use "".encode() or bytes("", "type of encoding, generally utf-8")
#
# send(data) Sends the specified data over the socket. It will attempt to send as much data as possible in a single call, up to the buffer size. 
#   If the buffer is full and not all data is sent, 
#   the unsent data remains in the buffer and must be sent manually by calling send() again.
# sendall(data): Sends all the data in the buffer over the socket. 
#   It repeatedly calls send() to send all the data until either all data has been sent or an error occurs. 
#   It ensures that all data is sent before returning, simplifying the process of sending large amounts of data.
#
# The server socket is used only for accepting connections.
# Once a connection is accepted, both the server and the client use the same client socket to communicate over the established connection.
#
# AF_INET refers to IPV4, SOCK_STREAM refers to TCP

# ------- Client side code -------
from socket import *

server_ip = '127.0.0.1'
server_port = 1234
buffer_size = 1024
data_to_share = b''

def connection(server_ip, server_port, buffer_size, data_to_share):

    # Creating a socket using the with statement
    with socket(AF_INET, SOCK_STREAM) as client_socket:

        # Connecting the server socket
        client_socket.connect((server_ip, server_port))

        # Sending data to the server using the client socket
        client_socket.sendall(data_to_share)

        # Receving data from the server using the client socket
        received_data = client_socket.recv(buffer_size).decode()

connection(server_ip, server_port, buffer_size, data_to_share)

# Client side code must be run on another terminal