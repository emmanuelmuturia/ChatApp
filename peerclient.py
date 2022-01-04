#!/usr/bin/env python3

from tkinter import *
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def sendMessage():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = entry2.get()
        s.sendall(message.encode('utf-8'))
        #s.sendall(b"Hello")

win = Tk()  
  
win.geometry("400x250")  
  
name = Label(win, text = "IP Address").place(x = 10,y = 50)  
  
message = Label(win, text = "Message").place(x = 10, y = 90)  
  
submitbtn = Button(win, text = "Send",activebackground = "red", activeforeground = "blue", command=sendMessage).place(x = 30, y = 170)  
  
entry1 = Entry(win).place(x = 80, y = 50)  

entry2 = Entry(win)
entry2.place(x = 80, y = 90)
#entry2 = Text(win, height=5, width=20).place(x = 150, y = 120)

win.mainloop()
