#!/usr/bin/env python3


import socket

HOST = '127.0.0.1'  # Standard loopback interface address for our local machine (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  #Define our sockets and protocol used i.e TCP...
    s.bind((HOST, PORT)) #Bind the server to the already defined IP Address and Port Number...
    s.listen() #Listen for new incoming connections...
    conn, addr = s.accept() #Accept the new connections...
    with conn:
        print('Connected by', addr) #Print message and the client's IP Address...
        while True:
            data = conn.recv(1024) #Define maximum bit size for the new connection...
            print(repr(data)) #Print the client's data...
            if not data:
                break #Break connection if no data is sent...
