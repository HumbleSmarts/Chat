import socket
# import sys
import time

## end of import ###

### init ###

s = socket.socket()
host = input(str("please enter the hostname of the server: "))
port = 8000
s.connect((host, port))
print("conneted to the chat server")
while 1:
    incoming_massage = s.recv(1024)
    incoming_massage = incoming_massage.decode()
    print("Server: " , incoming_massage)
    print("")
    massage = input(str(">> "))
    massage = massage.encode()
    s.send(massage)
    print("Massage has been sent....")
    print("")
