import socket
UPD_IP = 'localhsot'
UDP_PORT = 5005
MESSAGE = b'Hello , World!'
print("PORT %s" %UDP_PORT)
print("IP %s" % UPD_IP)
print("message : %s" % MESSAGE)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE,(UPD_IP,UDP_PORT))