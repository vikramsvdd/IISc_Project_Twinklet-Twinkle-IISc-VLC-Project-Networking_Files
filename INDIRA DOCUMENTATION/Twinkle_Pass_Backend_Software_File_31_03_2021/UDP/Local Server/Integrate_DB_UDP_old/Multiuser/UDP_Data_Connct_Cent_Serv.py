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

    host = "10.32.26.70"
    port = 5002             #port number for connection between local server and central server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # instantiate
    
    try:
        print("Connection Established to Central Server.")
        print("Client connected to Central Server:",host)

        if not data == '':
            client_socket.sendto(data.encode(), (host, port))  # send message
            print("Data sent successfully to Central Server")
            authentication_status = client_socket.recvfrom(1024)
            auth_stat = authentication_status[0].decode()
            print("authentication_status:",auth_stat)
    except ConnectionRefusedError:
        print("Unable to connect to Central Server")

    client_socket.close()  # close the connection

    return auth_stat

