import socket
#hostname = "twinkle-central-server"
#HOST = socket.gethostbyname(hostname)
HOST='192.168.1.4'
PORT=9998   # This port different from local server to central server port
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
msg="1*1*02/01/2022"                   #sno*twinklet_id*today's date
client.send(msg.encode('utf-8'))
print(client.recv(1024).decode('utf-8'))



