import numpy as np
import random
import time
import sqlite3
import socket
from datetime import datetime

global xc
global yc
xc, yc = 7, 25

def binary_to_decimal(arr):
	num = 0
	for i in range(len(arr)):
		num += arr[i]*np.power(2,i)
	return num

def binary_to_char(arr):
	num = 0
	for i in range(len(arr)):
		num += int(arr[i])*np.power(2,len(arr)-1-i)
		#print(num)
	return str(chr(num))

gene_countr=1
	
def binary_to_char_dec(arr):
	num = 0
	for i in range(len(arr)):
		num += int(arr[i])*np.power(2,len(arr)-1-i)
		#print(num)
	return num

sensor_data_base = ['Temperature: 23 Degrees Celsius', 'Temperature: 10 Degrees Celsius', 'Temperature: 37 Degrees Celsius', 'Temperature: 45 Degrees Celsius', 'Presuure: 760 mm', 'Presuure: 756 mm', 'Presuure: 736 mm', 'Presuure: 776 mm']

position_data_base = ['Room.no: 1.08 -ECE Department', 'Room.no: 1.09 -ECE Department', 'GSH-ECE Department', 'Wireless Research Lab-SP Building', 'Navacomm Lab-SP Building', 'Room.no: 309 -EE Department', 'Room.no: 315 -EE Department', 'Room.no: 204 -EE Department', 'Seminar Hall-CSA Department', 'Seminar Hall- Main Building',  'Seminar Hall- CeNSE']

def Random_Data_Generation():
    
    random_array = (np.random.uniform(0,1,32) > 0.5 ).astype(np.int32)
    splits = np.split(random_array,[16])
    name_rand = sensor_data_base[random.randint(0,7)]
    char_bits_ = [format(ord(x),'b') for x in name_rand]
    position_rand = position_data_base[random.randint(0,7)]
    position_bits_ = [format(ord(x),'b') for x in position_rand]
    
    twinkler_id = binary_to_decimal(splits[0])
    
    flashpoint_id = binary_to_decimal(splits[1])
    
    char = []
    for i in range(len(char_bits_)):
	     char.append(binary_to_char(char_bits_[i]))	
    data_vale=''.join(char)

    pos_char= []
    for i in range(len(position_bits_)):
	     pos_char.append(binary_to_char(position_bits_[i]))
	
    pos_vale=''.join(pos_char)

    now_time= datetime.now()
    data_remarks= "-No- "
    
    data_packett = "%s*%s*%s*%s*%s*%s"%(twinkler_id,flashpoint_id,pos_vale,now_time,data_vale, data_remarks)
    
    print (data_packett)
    print("\n")
    mySocket.connect((host,port))
    mySocket.send(message.encode())
    mySocket.close()
    after(5000,Random_Data_Generation)

if __name__ == "__main__":
        host = '10.32.240.88'
        port = 5000
        mySocket = socket.socket()
        Random_Data_Generation()