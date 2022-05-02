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

valid_twinklet_list={'1','2','6'}

#global time_client_to_server
arr_daily_data = np.array([])


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_over", action="store_true")
    return parser.parse_args()

global xc
global yc
xc, yc = 9, 25;

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added to Central Server: ", clientAddress)
    def run(self):
        global arr_daily_data
        print("Connection from local Server: ", clientAddress)
        msg = ''
        conn = sqlite3.connect('Twinkle_Database.db')  # Opens the SQL Database
        print("Opened database successfully")
        while True:
            try:
                data = self.csocket.recv(1024)
                msg = data.decode()

                if not msg == '':
                    time_after_data_recv = time.time()
                    print("time_after_data_recv:",time_after_data_recv)

                    time_client_to_server = time_after_data_recv - time_after_accept
                    print("time_client_to_server:",time_client_to_server)

                    arr_daily_data = np.append(arr_daily_data,time_client_to_server)
                    print("arr_daily_data:",arr_daily_data)
                    np.save("daily_delay_stats",arr_daily_data)

                    print("from local server", msg)
                    msg = msg + "*--*--"
                    twinklet_id = Datastoringfun(msg, conn)

                    print("twinklet_id:",twinklet_id,"\ttype:",type(twinklet_id))

                    if twinklet_id in valid_twinklet_list:
                        self.csocket.send('Authentication successful'.encode('utf-8'))
                    else:
                        self.csocket.send('Authentication unsuccessful'.encode('utf-8'))

                    print("Authentication Status sent")
                    daily_delay_statistics = np.load("daily_delay_stats.npy")
                    print("daily_delay_statistics: ",daily_delay_statistics)
                    print("\n")
            except UnicodeDecodeError:
                print("Error in Decoding the String")
            except AttributeError:
                print("Attribute Incorrect")

            process_daily_delay_stats()


def process_daily_delay_stats():
    global status_daily_delay_stat 
    curr_time = datetime.datetime.now()
    curr_time_hours = curr_time.strftime("%H")
    #curr_time_mins = int(curr_time.strftime("%M"))
    curr_time_mins = (curr_time.strftime("%M"))

    #print("curr_time_hours:",curr_time_hours,"\ttype(curr_time_hours):",type(curr_time_hours))
    #print("curr_time_mins:",curr_time_mins,"\ttype(curr_time_mins):",type(curr_time_mins))

    if curr_time_hours == "13":
         #if curr_time_mins >=43  and curr_time_mins < 44:
        if curr_time_mins =="00":
            if not status_daily_delay_stat:
                status_daily_delay_stat = 1
                print("In the process daily_delay_stats")
                daily_delay_stats = np.load("daily_delay_stats.npy")
                daily_delay_stats = np.sort(daily_delay_stats)
                daily_minimum = round(daily_delay_stats[0],4)
                daily_stats_len = len(daily_delay_stats)
                daily_maximum = round(daily_delay_stats[daily_stats_len - 1],4)
                daily_mean = round(np.mean(daily_delay_stats),4)
                daily_std_dev = round(np.std(daily_delay_stats),4)
 
     
                daily_stats_data = "min:{}".format(daily_minimum)+"\nmax:{}".format(daily_maximum)+"\nmean:{}".format(daily_mean)+"\nstd dev:{}".format(daily_std_dev)
                print("daily_stats_data:",daily_stats_data)
 
                msg = "--*--*--*--*--*--*" + daily_stats_data +"*--"

                conn1 = sqlite3.connect('Twinkle_Database.db')  # Opens the SQL Database
 
                Datastoringfun(msg,conn1)


#     if not status_daily_delay_stat:
#         status_daily_delay_stat = 1
#         print("In the process daily_delay_stats")
#         daily_delay_stats = np.load("daily_delay_stats.npy")
#         daily_delay_stats = np.sort(daily_delay_stats)
#         daily_minimum = daily_delay_stats[0]
#         daily_stats_len = len(daily_delay_stats)
#         daily_maximum = daily_delay_stats[daily_stats_len - 1]
#         daily_mean = np.mean(daily_delay_stats)
#         daily_std_dev = np.std(daily_delay_stats)
# 
#         daily_stats_data = "min:{}".format(daily_minimum)+"\nmax:{}".format(daily_maximum)+"\nmean:{}".format(daily_mean)+"\nstd dev:{}".format(daily_std_dev)
#         print("daily_stats_data:",daily_stats_data)
# 
#         msg = "--*--*--*--*--*--*" + daily_stats_data +"*--"
# 
#         conn1 = sqlite3.connect('Twinkle_Database.db')  # Opens the SQL Database
# 
#         Datastoringfun(msg,conn1)


def Datastoringfun(data_element, conn):
    global count
    global data_base
    global local_count
    
    print(local_count+1)
    local_count += 1
    data_split = data_element.split('*')
    print(data_split)
    split_count = local_count
    split_twinkler_id = data_split[0]
    split_flashpoint_id = data_split[1]
    split_pos_vale = data_split[2]
    split_now_time = data_split[3]
    split_data_vale = data_split[4]
    split_data_remarks = data_split[5]
    split_daily_delay_stats = data_split[6]
    split_cumulative_delay_stats = data_split[7]
          
    conn.execute('''INSERT INTO TWINKLE_DATA (SRNO,TWINKLERID,FLASHPOINTID,FLASHPOS,DATETIME,DATA_PACK,REMARKS,DAILY_DELAY_STATISTICS,CUMULATIVE_DELAY_STATISTICS) VALUES(?,?,?,?,?,?,?,?,?)''', (split_count, split_twinkler_id, split_flashpoint_id, split_pos_vale, (dt.datetime.now()).strftime("%c"), split_data_vale, split_data_remarks,split_daily_delay_stats,split_cumulative_delay_stats))
    conn.commit()
    print("inserted data ")
    print(split_count)
    #print("\n")
    iter_count = int(local_count)
    count = local_count
    np.save("checkpoint", count)
    return split_twinkler_id


if __name__ == "__main__":
    global count
    global local_count
    global time_after_accept
    global time_after_data_recv
    global time_client_to_server

    status_daily_delay_stat=0

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
    port = 20000
    Serv_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Use only for TCP
    Serv_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Serv_Socket.bind((host, port)) #Serv_Socket.bind((host,port))
    print("Namaste..!")
    print("Central Server started")
    print("Waiting for local server..")
    local_count = int(count)
    while True:
        #process_daily_delay_stats()
        Serv_Socket.listen(1)
        #process_daily_delay_stats()
        clientsock, clientAddress = Serv_Socket.accept()
        print("Connection accepted...")
        time_after_accept = time.time()
        print("time_after_accept:",time_after_accept)
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
        
        
    
    clientsock.close()

