########################################## UDP Socket Program ################################################3
from tkinter import *
import numpy as np
import socket, threading
import random
import datetime as dt
import threading
import argparse
import sqlite3
import time
from datetime import datetime
import datetime


#list of valid TwinkleT's for TwinkleR:1
list_valid_twinklet_for_twinkler1={'1','2','6','5'}


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_over", action="store_true")
    return parser.parse_args()

global xc
global yc
xc, yc = 7, 25;

#class ClientThread(threading.Thread):
#    def __init__(self):
#        threading.Thread.__init__(self)
#        self.csocket = clientsocket
#        print("New connection added to Central Server: ", clientAddress)
#    def run(self):
#        print("Connection from local Server: ", clientAddress)

def DataStoringfun(conn):
    global count
    global data_base
    global local_count
   
    Serv_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Use only for UDP
    Serv_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Serv_Socket.bind((host, port)) #Serv_Socket.bind((host,port))
    print("Namaste..!")
    print("Central Server started")
    print("Waiting for local server..")

    msg = ''
    while True:
        try:
            data = Serv_Socket.recvfrom(1024)
            msg = data[0]
            addr = data[1]
            msg = msg.decode()

            if not msg == '':
                print(local_count+1)
                local_count += 1
                data_split = msg.split('*')
                print(data_split)
                split_count = local_count
                split_twinkler_id = data_split[0]
                split_flashpoint_id = data_split[1]
                split_pos_vale = data_split[2]
                split_now_time = data_split[3]
                split_data_vale = data_split[4]
                split_data_remarks = data_split[5]
          
                conn.execute('''INSERT INTO TWINKLE_DATA (SRNO,TWINKLERID,FLASHPOINTID,FLASHPOS,DATETIME,DATA_PACK,REMARKS) VALUES(?,?,?,?,?,?,?)''', (split_count, split_twinkler_id, split_flashpoint_id, split_pos_vale, (dt.datetime.now()).strftime("%c"), split_data_vale, split_data_remarks))
                conn.commit()
                print("inserted data ")
                print(split_count)
                #print("\n")
                iter_count = int(local_count)
                count = local_count
                np.save("checkpoint", count)
                
                twinklet_id = split_twinkler_id
                twinkler_id = split_flashpoint_id

                #Sending Authentication STATUS for TwinkleR 1
                if twinklet_id in list_valid_twinklet_for_twinkler1:
                    Serv_Socket.sendto('Open'.encode(), addr)
                    print("Door Open for twinklet_id:",twinklet_id)
                else:
                    Serv_Socket.sendto('Dont_open'.encode(), addr)
                    print("Door Close for twinklet_id:",twinklet_id)

                print("Authentication Status sent")
                print("\n")
        except UnicodeDecodeError:
            print("Error in Decoding the String")
        except AttributeError:
            print("Attribute Incorrect")


if __name__ == "__main__":
    conn = sqlite3.connect('Twinkle_Database.db')  # Opens the SQL Database
    print("Opened database successfully")
    
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

    host = "0.0.0.0"
    port = 5002                 #port for connection between local and central server
    local_count = int(count)

    DataStoringfun(conn)
    conn.close()
    
