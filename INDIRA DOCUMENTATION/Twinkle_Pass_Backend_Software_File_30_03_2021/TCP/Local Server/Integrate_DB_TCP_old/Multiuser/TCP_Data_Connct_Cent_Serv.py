import socket
import time
import numpy as np
import sqlite3
import datetime as dt 
from datetime import datetime

def send_local_data(msg):
    data = msg
    auth_stat = client_program(data)
    return auth_stat

def get_local_data():
    return data

def client_program(data):
    host_ip = "10.32.26.70"

    host = host_ip
    port = 5002  # socket server port number

    client_socket = socket.socket()  # instantiate
    
    try:
        client_socket.connect((host, port))  # connect to the server
        print("Connection Established to Central Server.")
        print("Client connected to Central Server:",host)

        if not data == '':
            client_socket.send(data.encode())  # send message
            print("Data sent successfully to Central Server")
            auth_stat = client_socket.recv(1024).decode()
            print("authentication_status:",auth_stat)
    except ConnectionRefusedError:
        print("Unable to connect to Central Server")

    client_socket.close()  # close the connection

    return auth_stat

