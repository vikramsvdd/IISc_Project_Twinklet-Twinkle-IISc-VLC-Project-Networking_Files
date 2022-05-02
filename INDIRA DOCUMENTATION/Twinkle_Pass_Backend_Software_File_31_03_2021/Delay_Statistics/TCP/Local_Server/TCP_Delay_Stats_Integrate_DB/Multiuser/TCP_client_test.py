import socket
import time

def client_program():
    host = '127.0.0.1'
    port = 19000  # socket server port number

    client_socket = socket.socket()
    client_socket.connect((host, port))

    i = 1

    while i<=1:

        client_socket.send(message1.encode('utf-8'))  # send message
        print("Message1 Sent Successfully")
#        time.sleep(27)
#        client_socket.send(message4.encode('utf-8'))  # send message
#        print("Message4 Sent Successfully")
#        time.sleep(43)
#        client_socket.send(message2.encode('utf-8'))  # send message
#        print("Message2 Sent Successfully")
#        time.sleep(99)
#        client_socket.send(message3.encode('utf-8'))  # send message
#        print("Message3 Sent Successfully")
#        time.sleep(20)
#        client_socket.send(message5.encode('utf-8'))  # send message
#        print("Message5 Sent Successfully")
#
#        time.sleep(120)
#        client_socket.send(message1.encode('utf-8'))  # send message
#        print("Message1 Sent Successfully")
#        time.sleep(54)
#        client_socket.send(message4.encode('utf-8'))  # send message
#        print("Message4 Sent Successfully")
#        time.sleep(10)
#        client_socket.send(message2.encode('utf-8'))  # send message
#        print("Message2 Sent Successfully")
#        time.sleep(64)
#        client_socket.send(message3.encode('utf-8'))  # send message
#        print("Message3 Sent Successfully")
#        time.sleep(149)
#        client_socket.send(message5.encode('utf-8'))  # send message
#        print("Message5 Sent Successfully")
        
        i+=1 

    client_socket.close()  # close the connection


if __name__ == '__main__':
    global message
    message1 = "1*1*Broadband Wireless Lab*2020-02-03 17:21*Twinkle 1*Correct"
    message2 = "2*1*Broadband Wireless Lab*2020-02-03 17:21*Twinkle 2*Correct"
    message3 = "3*1*Broadband Wireless Lab*2020-02-03 17:21*Twinkle 3*Correct"
    message4 = "4*1*Broadband Wireless Lab*2020-02-03 17:21*Twinkle 4*Correct"
    message5 = "5*1*Broadband Wireless Lab*2020-02-03 17:21*Twinkle 5*Correct"
    client_program()

