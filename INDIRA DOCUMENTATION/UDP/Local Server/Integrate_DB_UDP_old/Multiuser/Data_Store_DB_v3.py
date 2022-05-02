from tkinter import *
import numpy as np
import socket, threading
import random
import datetime as dt
import threading
import argparse
import sqlite3
from datetime import datetime

from Data_Connct_Cent_Serv import *

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_over", action="store_true")
    return parser.parse_args()

global xc
global yc
xc, yc = 7, 25;


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added to local server: ", clientAddress)
    def run(self):
        print("Connection from local client: ", clientAddress)
        msg = ''
        conn = sqlite3.connect('Twinkle_Database.db')  # Opens the SQL Database
        print("Opened database successfully")
        while True:
            try:
                data = self.csocket.recv(1024)
                msg = data.decode()

#                if not msg == '':
#                    print("from local client",msg)
#                    Datastoringfun(msg, conn)
#                    #send_local_data(msg)
#                    print("\n")  

                print("from local client",msg)
                Datastoringfun(msg, conn)
                auth_status = send_local_data(msg)
                print("Authentication Key:",auth_status)
                #self.csocket.send(auth_status.encode('utf-8'))
                #print("Authentication key sent to TwinkleR")
                print("\n")
            except UnicodeDecodeError:
                print("Error in Decoding the String\n")
            except AttributeError:
                print("Attribute Incorrect\n")
        
def Datastoringfun(data_element, conn):
    global count
    global data_base
    global local_count
    
    #local_count+=1
    print(local_count+1)
    local_count += 1
#    if not data_element:    break
    data_split = data_element.split('*')
    #print(data_split)
    split_count = local_count
    split_twinkler_id = data_split[0]
    split_flashpoint_id = data_split[1]
    split_pos_vale = data_split[2]
    split_now_time = data_split[3]
    split_data_vale = data_split[4]
    split_data_remarks = data_split[5]
          
    conn.execute('''INSERT INTO TWINKLE_DATA (SRNO,TWINKLERID,FLASHPOINTID,FLASHPOS,DATETIME,DATA_PACK,REMARKS)
                            VALUES(?,?,?,?,?,?,?)''', (split_count, split_twinkler_id, split_flashpoint_id, split_pos_vale, (dt.datetime.now()).strftime("%c"), split_data_vale, split_data_remarks))
    conn.commit()
    print("inserted data ")
    print(split_count)
    iter_count = int(local_count) 
    count = local_count
    np.save("checkpoint", count)


if __name__ == "__main__":
    global count
    global local_count

    count = 0
    args = get_arguments()
    if args.start_over is True:
        count = 0
    else:
        try:
            count = np.load("checkpoint.npy")
        except:
            count = 0

    host = "10.32.26.20"            #Host IP Address
    port = 5000
    Serv_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Use only for TCP
    Serv_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Serv_Socket.bind((host, port)) #Serv_Socket.bind((host,port))
    print("Namaskaaram Andi")
    print("Local Server started")
    print("Waiting for client request..")
    local_count = int(count)
    while True:
        Serv_Socket.listen(1)
        clientsock, clientAddress = Serv_Socket.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()

    Serv_Socket.listen(1)
    Connct, addr = Serv_Socket.accept()
    print("connection established")
    print("Connection from: " + str(addr))

    Datastoringfun()
    
    Connct.close()    
    clientsock.close()  
