import socket
import time
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
is_send = True
counter = 1
while is_send:
    start = None
    if counter <= 6:
        string = input('Please input string ==  ')
        client_socket.sendto(str.encode(string),('localhost',20001))
        start = time.time()
        print('current time' ,start)
    else:
        is_send = False

    print(client_socket.recvfrom(1024))
    end = time.time()
    elapsed = end - start
    print('elapsed ===  ', elapsed)
    counter += 1
    
    