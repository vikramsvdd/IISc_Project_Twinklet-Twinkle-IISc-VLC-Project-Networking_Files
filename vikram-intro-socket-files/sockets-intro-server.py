import socket
HOST="192.168.1.3"
PORT=9999
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print("Server Started")


while True:                                    # can try messing with the loop
    communication_socket,address=server.accept()
    print("Waiting for client request, waiting ")
    print("Connected to",address)
    message=communication_socket.recv(1024).decode('utf-8')
    print("The Message is",message)
    communication_socket.send("Got your message ".encode('utf-8'))
    communication_socket.close()
    print("connection with",address,"Ended")
    print("Type of the message is ",type(message))
          
