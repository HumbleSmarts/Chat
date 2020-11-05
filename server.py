import socket
#import sys
import time

## end of import ###

### init ###

s = socket.socket()
host = socket.gethostname()
print("Server will be running on hosthost: ",host)
port = 8000
s.bind((host,port))
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr,"has connected to the server and is now online....")
print("")

while 1:
    massage = input(str(">> "))
    massage = massage.encode()
    conn.send(massage)
    print("Massage has been sent....")
    print("")
    incoming_massage = conn.recv(1024)
    incoming_massage = incoming_massage.decode()
    print("Client: ", incoming_massage)
    print("")

else:
    
    print("Desconneted")

