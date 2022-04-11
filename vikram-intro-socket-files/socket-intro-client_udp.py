import socket

msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("192.168.1.2", 20001)

# Create a UDP socket at client side

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

client.sendto(bytesToSend, serverAddressPort)

msgFromServer = client.recvfrom(1024)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
