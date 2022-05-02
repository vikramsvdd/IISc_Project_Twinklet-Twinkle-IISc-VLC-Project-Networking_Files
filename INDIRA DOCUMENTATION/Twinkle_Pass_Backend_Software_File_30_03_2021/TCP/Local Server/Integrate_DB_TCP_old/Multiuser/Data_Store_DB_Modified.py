from tkinter import *
import numpy as np
import socket
import random
import datetime as dt
import threading
import argparse
import sqlite3
from datetime import datetime

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_over", action="store_true")
    return parser.parse_args()

global xc
global yc
xc, yc = 7, 500;
 
        
def Datastoringfun():
    global count
    global data_base
    global local_count
    
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #Use only for TCP
    serv_socket.bind((host, port))                                      #Serv_Socket.bind((host,port))
    print("Namaskaaram Andi")
    serv_socket.listen(1)                                               #Wait for IP
    print("Listening...")
    connct, addr = serv_socket.accept()                                 #Establish Connection
    print("Accepted...")
    #serv_socket.settimeout(None)                                        #Added on 2020-Jan-25: Prevents Timeout
    print("connection established")
    print("Connection from: " + str(addr))
    
    while True:
        try:
            #a = dt.datetime.now()
            #local_count += 1
            print(local_count+1)
            print("Before receiving data_element")
            print("time: ", (dt.datetime.now()).strftime("%c"))
            data_element = connct.recv(1024).decode()                      #Use with TCP
            print("After receiving data_element")
            print("data_element: ", data_element)
            local_count += 1
            
            #if not data_element: break
            
            if not data_element:
                print("Entered not data_element block")
                connct.send(msg.encode('utf-8'))
                serv_socket.listen(1)                                       #Wait for IP
                connct, addr = serv_socket.accept()
                data_element = connct.recv(1024).decode()
                print("Exiting not data_element block")
                
            if data_element == '':
                print("Entered data_element == '' block")
                serv_socket.listen(1)
                connct, addr = serv_socket.accept()
                data_element = connct.recv(1024).decode()
                print("Exiting data_element == '' block")
            else:
                print("Entered else block")
                data_split = data_element.split('*')
                print(data_split)
                split_count = local_count
                split_twinkler_id = data_split[0]
                split_flashpoint_id = data_split[1]
                split_pos_vale = data_split[2]
                split_now_time = data_split[3]
                split_data_vale = data_split[4]
                split_data_remarks = data_split[5]
                split_data_remarks = "OK (TCP)"
                conn.execute('''INSERT INTO TWINKLE_DATA (SRNO,TWINKLERID,FLASHPOINTID,FLASHPOS,DATETIME,DATA_PACK,REMARKS)
                                VALUES(?,?,?,?,?,?,?)''', (split_count, split_twinkler_id, split_flashpoint_id, split_pos_vale, (dt.datetime.now()).strftime("%c"), split_data_vale, split_data_remarks))
                conn.commit()
                print("inserted data ")
                print(split_count)
                iter_count = int(local_count)
                count = local_count
                np.save("checkpoint", count)
                print("Exiting else block")
                print("\n")
                
        except UnicodeDecodeError:
            print("Error in Decoding the String")
        except AttributeError:
            print("Attribute Incorrect")    
        

if __name__ == "__main__":
    conn = sqlite3.connect('Twinkle_Database.db')                              #Opens the SQL Database
    print("Opened database successfully")
    
    global count
    global local_count
    global connct
    count = 0
    args = get_arguments()
    if args.start_over is True:
        count = 0
    else:
        try:
            count = np.load("checkpoint.npy")
        except:
            count = 0
    host = "127.0.0.1"                                                       #Host IP Address
    #host = "0.0.0.0"
    port = 6000
    msg = "OK"
    
    local_count = int(count)
    Datastoringfun()
    connct.close()
