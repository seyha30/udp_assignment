import socket
import sys
sock  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',10000)
sock.bind(server_address)
while True:
    data, address = sock.recvfrom(4096)
    if data:
        print('received data' + data.decode('utf-8'))
        sent = sock.sendto(data.endcode('utf-8'),address)
    