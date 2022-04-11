from tkinter import *
#import numpy as np
import socket, threading
import random
import datetime as dt
import threading
import argparse
import sqlite3
import time
from datetime import datetime
from datetime import date
dbc=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]  # month name bro



def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_over", action="store_true")
    return parser.parse_args()

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added to Central Server: ", clientAddress)
    def run(self):
        print("Connection from local Server: ", clientAddress)
        msg = ''
        conn = sqlite3.connect('winkle.db')  # Opens the SQL Database
        print("Opened database successfully")
        c=conn.cursor()
        c.execute('SELECT * FROM twinkle')   #reading from the table
        fetchall=c.fetchall()
        print(fetchall)              # you might know why the below lines don't work , you first need to select
        twinklet_idarray=[]
        for row in fetchall:
            twinklet_idarray.append(row[1])
        print(twinklet_idarray)
        
        while True:
            try:
                data = self.csocket.recv(1024)
                msg = data.decode()

                if not msg == '':
                    twinklet_id = Datastoringfun(msg, conn)
                    day = dayobtain(msg,conn)   #obtaining the day from the message
                    month=monthobtain(msg,conn)

#                    print("twinklet_id:",twinklet_id,"\ttype:",type(twinklet_id))

                    if twinklet_id in twinklet_idarray:
                        self.csocket.send('Open'.encode('utf-8'))
                        auth_status='Open'
                    else:
                        self.csocket.send('Dont_open'.encode('utf-8'))
                        auth_status='Dont_Open'
                        
                    print("Authentication Status sent")
                    print("\n")
                    attendancemark(auth_status,twinklet_id,day,month)      #Marking the attendance buddy
                    
            except UnicodeDecodeError:
                print("Error in Decoding the String")
            except AttributeError:
                print("Attribute Incorrect")

def Datastoringfun(data_element, conn):
    data_element=data_element.split('*')
    sno= data_element[0]
    twinklet_id = int(data_element[1])
    return twinklet_id

def dayobtain(data_element,conn):
         data_element=data_element.split('*')          ## OBTAINING DAY(EMBEDDED IN THE MESSAGE) BY SPLICING THE MESSAGE
         date= data_element[2]
         datelist=date.split("/")
         day=datelist[0]
         day=int(day)
         day=str(day)
         return day

def monthobtain(data_element,conn):
         data_element=data_element.split('*')          ## OBTAINING Month(EMBEDDED IN THE MESSAGE) BY SPLICING THE MESSAGE
         date= data_element[2]
         datelist=date.split("/")
         month=datelist[1]
         for i in range(len(dbc)):
             if(int(month)==i+1):
                 mont=dbc[i]
         return mont      
        
def markabsentinitial(): #initially when the day starts, i mark absemt for everybody, if they are present, this 'a' will get replaced!!!!
    today = date.today()
    day=today.strftime("%d")
    month = today.strftime("%m")
    mont=''
    for i in range(len(dbc)):
        if(int(month)== i+1):
            mont=dbc[i]
    conn2= sqlite3.connect(mont+'.db')
    d=conn2.cursor()
    print("Opened Database",mont)
    d.execute('SELECT * FROM twinkle')
    day1="day"+day
    d.execute('UPDATE twinkle SET '+day1+'="a"')
    conn2.commit()
    d.close()
    conn2.close()
    

def attendancemark(auth_status,twinklet_id,day,month):
        conn1 = sqlite3.connect(month+'.db')  
        print("Opened database successfully "+month)
        d=conn1.cursor()
        d.execute('SELECT * FROM twinkle')
        fetchalll=d.fetchall()
        day1="day"+day
        if(auth_status=='Open'):
            for row in fetchalll:
                if(twinklet_id==row[1]):
                    d.execute('UPDATE twinkle SET '+day1+'="p" WHERE twinkletid= ? ',(row[1],))
                
            conn1.commit()
            d.close()
            conn1.close()














if __name__ == "__main__":
    global count
    global local_count
    global auth_status
    global twinklet_id
    global day                          
                              

    count = 0
    args = get_arguments()
    if args.start_over is True:
        count = 0
    else:
        try:
            count = np.load("checkpoint.npy")
        except:
            count = 0
    host = "192.168.1.2"  #Ip adress
    port = 9999
    Serv_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Use only for TCP
    Serv_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Serv_Socket.bind((host, port)) #Serv_Socket.bind((host,port))
    print("Vanakkam ..!")
    print("Central Server started")
    print("Waiting for local server..")
    markabsentinitial()                                    #refer to the definition
    #local_count = int(count)
    while True:
        Serv_Socket.listen(1)
        clientsock, clientAddress = Serv_Socket.accept()
        print("Connection accepted...")
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
    
    clientsock.close()
