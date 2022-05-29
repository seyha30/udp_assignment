import sys
import socket
# create UDP scoket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost',10000)
message = 'Preparing message for server'
try:
    sent = sock.sendto(message.encode('utf-8'),server_address)
    data,server = sock.recvfrom(4096)
    print(data)
finally:
    sock.close()