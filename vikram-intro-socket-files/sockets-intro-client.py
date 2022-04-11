import socket
import datetime
HOST='192.168.1.3'
PORT=9999
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))     #TCP connection established
send_time_ms = datetime.datetime.now()
client.send("stuff".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
recv_time_ms = datetime.datetime.now()
rtt_in_ms = recv_time_ms - send_time_ms
print("The Latency is ",rtt_in_ms.total_seconds() * 1000)





