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
    parser.add_argument("--start_over" ,action = "store_true")
    return parser.parse_args()

	
global xc
global yc
xc, yc = 7, 25;
 
        
def Datastoringfun():
    global count
    global data_base
    global local_count
    while True:
          #a = dt.datetime.now()
          local_count+=1
          print(local_count)
          #data_element = Connct.recv(1024).decode()  #Use with TCP
          data_element = Serv_Socket.recv(1024).decode()
          data_split = data_element.split('*')
          print(data_split)
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
          print("\n")
          iter_count=int (local_count)
          count= local_count
          np.save("checkpoint",count)
   
        




if __name__ == "__main__":
    conn = sqlite3.connect('Twinkle_Database.db') #Opens the SQL Database
    print ("Opened database successfully")
    
    global count
    global local_count
    count = 0
    args = get_arguments()
    if args.start_over == True:
        count = 0
    else :
        try :
            count = np.load("checkpoint.npy")
        except :
            count = 0
    host = "10.32.26.16" #Host IP Address
    port = 5000 
    #Serv_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP Mode
    Serv_Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP Mode
    Serv_Socket.bind((host,port)) #Serv_Socket.bind((host,port))
    print("Namaskaaram Andi")
    #Serv_Socket.listen(1)         #Wait for IP #TCP
    #Connct, addr = Serv_Socket.accept() #Establish Connection #Use with TCP
    #print("connecton established")  #Use with TCP
    #print ("Connection from: " + str(addr)) #Use with TCP
    local_count = int (count)
    Datastoringfun()
    #Connct.close() #Use with TCP
    
