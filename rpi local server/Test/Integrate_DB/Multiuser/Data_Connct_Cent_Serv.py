import socket


def send_local_data(msg):
    data = msg
    client_program(data)

def get_local_data():
    return data

def client_program(data):
    f = open("/home/pi/Desktop/Integrate_DB/Multiuser/tunnel_ip_addr","r")
    host_ip = f.read()
    host = host_ip
    port = 21001  # socket server port number

    client_socket = socket.socket()  # instantiate
    
    try:
        client_socket.connect((host, port))  # connect to the server
        print("Connection Established to Central Server.")
        print("Client connected to Central Server:",host)

        #print("data:",data)
    
        if not data == '':
            client_socket.send(data.encode())  # send message
            print("Data sent successfully to Central Server")
            authentication_status = client_socket.recv(1024).decode()
            print("authentication_status:",authentication_status)
    except ConnectionRefusedError:
        print("Unable to connect to Central Server")

#                data = client_socket.recv(1024).decode()  # receive response

    client_socket.close()  # close the connection

