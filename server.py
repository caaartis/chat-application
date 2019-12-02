import socket
import sys
import time

#end of imports


#init
s=socket.socket()
host =socket.gethostname()

#set up the port

print("Server will be runing on the host ", host)
port=8000

#bind socket with gethostname
s.bind((host,port))
print("")
print("Server done bind to host and port successfully")
print("")
print("Server is waiting for incoming connections")
s.listen(1)
conn,addr=s.accept()
print(addr,"Has connected to the server and is now online")
print("")


#Now sound packets accross and it will officially be a chat program
while 1:


        message=input(str(">>"))
        #convert message variable into bytes

        message=message.encode()
        conn.send(message)
        print("Message have been sent ....")
        print("")
        incoming_message=conn.recv(1024)
            #Now you need to decode message so it can be displayed on client screen

        incoming_message=incoming_message.decode()
        print("Client:",incoming_message)
        print("")
