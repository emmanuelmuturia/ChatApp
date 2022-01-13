#!/usr/bin/env python3

import socket
import threading


HOST = '127.0.0.1'
PORT = 9090


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #DEfine your sockets and protocol used i.e TCP
server.bind((HOST, PORT)) #Bind the server to the defined IP Address and Port Number...

server.listen() #Listen for new incoming connections...


clients = [] #Inititalize an empty array for storing the clients...
nicknames = [] #Initialize an empty array for storing nicknames...

def broadcast(message): #Function to send message in the chatroom...
    for client in clients:
        client.send(message)


def handle(client): #Function to handle client's message and broadcast it...
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}) says {message}")
            broadcast(message)
        except: #Remove the pre entered input by the client if anything goes wrong and close the program...
            index = clients.index(client)
            clients.remove(client)
            clients.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receive(): #Function to receive new connection, append the details to the array and broadcast the message and sender details...
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)


        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} has joined the chat!\n".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))
        
        thread = threading.Thread(target=handle, args=(client,)) #Define threading that takes the multiple clients as one of the arguments...
        thread.start() #Enable threading where multiple clients can connect and send messages at the same time on the same chatroom...

print("Server running...")
receive()  #Invoke the receive() function...      
