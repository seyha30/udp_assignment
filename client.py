import socket
import time
client_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
file = open('log.txt','a')
is_send = True
counter = 1
while is_send:
    start = None
    if counter <= 10:
        string = input('Please input message :  ')
        client_socket.sendto(str.encode(string),('localhost',20001))
        start = time.time()
        print('current time' ,start) 
    else:
        is_send = False
    print(client_socket.recvfrom(1024))
    end = time.time()
    elapsed = end - start
    print('Elapsed time ===  ', elapsed)
    counter += 1
    file.write(str(elapsed))
    file.write('\n')
    file.flush()
file.close()
    
    