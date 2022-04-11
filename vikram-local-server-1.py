from tkinter import *
#import numpy as np
import socket, threading
import random
import datetime as dt
import threading
import argparse
import sqlite3
from datetime import datetime

from localcentralconnectionprog import *

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_over", action="store_true")
    return parser.parse_args()



class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added to local server: ", clientAddress)
    def run(self):
        print("Connection from local client: ", clientAddress)
        while True:
            try:
                data = self.csocket.recv(1024)
                msg = data.decode()

                if not msg == '':
                    print("from local client",msg)
                    auth_status = send_local_data(msg)
                    print("Authentication Key:",auth_status)    # what is happening here?
                    self.csocket.send(auth_status.encode('utf-8'))
                    print("\n")    
            except UnicodeDecodeError:
                print("Error in Decoding the String")
            except AttributeError:
                print("Attribute Incorrect")
        
if __name__ == "__main__":              # WHY IS THIS?
  
    count = 0
    args = get_arguments()
    if args.start_over is True:
        count = 0
    else:
        try:
            count = np.load("checkpoint.npy")
        except:
            count = 0


    host = "192.168.1.2"
    port = 9998
    Serv_Socket1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Serv_Socket1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Serv_Socket1.bind((host, port))
    print("Vanakkam Central Server")
    print("Local Server started")
    print("Waiting for client request..")
    local_count = int(count)
    while True:
        Serv_Socket1.listen(1)
        clientsock, clientAddress = Serv_Socket1.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
        
    clientsock.close()    
