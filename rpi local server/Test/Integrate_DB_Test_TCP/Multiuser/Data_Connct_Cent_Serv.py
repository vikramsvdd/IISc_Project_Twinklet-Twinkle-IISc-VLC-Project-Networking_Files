import socket
import time
import numpy as np
import sqlite3
import datetime as dt 
from datetime import datetime

arr_delay_stats = np.array([])

def send_local_data(msg):
    data = msg
    client_program(data)

def get_local_data():
    return data

def client_program(data):
    f = open("/home/pi/Desktop/Integrate_DB/Multiuser/tunnel_ip_addr","r")
    host_ip = f.read()

    global arr_delay_stats

    host = host_ip
    port = 20000  # socket server port number

    client_socket = socket.socket()  # instantiate
    
    try:
        time_before_connct = time.time()
        client_socket.connect((host, port))  # connect to the server
        print("Connection Established to Central Server.")
        print("Client connected to Central Server:",host)

        if not data == '':
            #print("data before sending to central:",data)
            client_socket.send(data.encode())  # send message
            print("Data sent successfully to Central Server")
            authentication_status = client_socket.recv(1024).decode()
            print("authentication_status:",authentication_status)
            time_after_auth_recv = time.time()
            time_taken_comm = round(time_after_auth_recv - time_before_connct, 5)
            print("time_before_connct:",time_before_connct,"\ttime_after_auth_recv:",time_after_auth_recv,"\ttime_taken_comm:",time_taken_comm)
            data = data + "*--"
            enter_delay_stats(data,time_taken_comm)
    except ConnectionRefusedError:
        print("Unable to connect to Central Server")

#                data = client_socket.recv(1024).decode()  # receive response

    client_socket.close()  # close the connection

    arr_delay_stats = np.load("/home/pi/Desktop/Test/Integrate_DB_Test_TCP/Multiuser/Delay_Stats/chkpoint_stats.npy")
    arr_delay_stats_len = len(arr_delay_stats)
    #print("\narr_delay_stats:", arr_delay_stats)
    #print("arr_delay_stats_len:",arr_delay_stats_len,"\ttype(arr_delay_stats_len):",type(arr_delay_stats_len),"\n")

    if arr_delay_stats_len == 5:
        arr_delay_stats = np.sort(arr_delay_stats)
        arr_delay_stats_min = round(arr_delay_stats[0],4)
        arr_delay_stats_max = round(arr_delay_stats[arr_delay_stats_len - 1],4)
        arr_delay_stats_mean = round(np.mean(arr_delay_stats),4)
        arr_delay_stats_std_dev = round(np.std(arr_delay_stats),4)
 
        delay_stats_data = "min:{}".format(arr_delay_stats_min)+"\nmax:{}".format(arr_delay_stats_max)+"\nmean:{}".format(arr_delay_stats_mean)+"\nStd dev:{}".format(arr_delay_stats_std_dev)
        #print("delay_stats_data:",delay_stats_data)
 
        msg = "--*--*--*--*--*--*" + delay_stats_data

        enter_delay_stats(msg,"--")
        print("Statistics inserted in database")

        arr_delay_stats = np.array([])
        np.save("/home/pi/Desktop/Test/Integrate_DB_Test_TCP/Multiuser/Delay_Stats/chkpoint_stats",arr_delay_stats)


def enter_delay_stats(data,time_taken_comm):
    global arr_delay_stats
    #print("data:",data)
    #print("time_taken_comm:",time_taken_comm)
    
    count_delay_stats = 0
    count_delay_stats = np.load("/home/pi/Desktop/Test/Integrate_DB_Test_TCP/Multiuser/Delay_Stats/checkpoint_delay.npy")
    local_count_delay_stats = int(count_delay_stats)
    
    conn_delay_stats = sqlite3.connect('/home/pi/Desktop/Test/Integrate_DB_Test_TCP/Multiuser/Delay_Stats/Twinkle_Delay_Stats_Database.db')
    print("Opened the database to save delay statistics successfully")

    print(local_count_delay_stats+1)
    local_count_delay_stats += 1
    data_split = data.split('*')
    #print(data_split)
    split_count_delay_stats = local_count_delay_stats
    split_twinklet_id = data_split[0]
    split_twinkler_id = data_split[1]
    split_pos_vale = data_split[2]
    split_now_time = data_split[3]
    split_data_value = data_split[4]
    split_data_remarks = data_split[5]
    delay_stats = data_split[6]

    conn_delay_stats.execute('''INSERT INTO TWINKLE_DELAY_STATS_DATA (SRNO,TWINKLETID,TWINKLERID,DATETIME,DATA_PACK,DELAY,STATISTICS) VALUES(?,?,?,?,?,?,?)''',(split_count_delay_stats, split_twinklet_id, split_twinkler_id, dt.datetime.now(), split_data_value, time_taken_comm, delay_stats))
    conn_delay_stats.commit()
    print("inserted data in delay statistics")
    print(split_count_delay_stats)
    count_delay_stats = local_count_delay_stats
    np.save("/home/pi/Desktop/Test/Integrate_DB_Test_1/Multiuser/Delay_Stats/checkpoint_delay", count_delay_stats)

    arr_delay_stat = np.load("/home/pi/Desktop/Test/Integrate_DB_Test_TCP/Multiuser/Delay_Stats/chkpoint_stats.npy")
    arr_delay_stat = np.append(arr_delay_stat,time_taken_comm)
    np.save("/home/pi/Desktop/Test/Integrate_DB_Test_TCP/Multiuser/Delay_Stats/chkpoint_stats", arr_delay_stat)

    conn_delay_stats.close()

