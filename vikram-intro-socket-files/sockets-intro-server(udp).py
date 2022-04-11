import socket
HOST= "192.168.1.2"
PORT = 20001
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Bind to address and ip

server.bind((HOST, PORT))

print("UDP server up and listening")

 # Listen for incoming datagrams

while(True):

    bytesAddressPair = server.recvfrom(1024)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   # Sending a reply to client

    server.sendto(bytesToSend, address)
