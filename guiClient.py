from tkinter import *
import socket
from threading import Thread
from time import sleep
import random

root = Tk()
root.title("Chat App")

Inputframe = Frame(root, width = 1000, height = 100)
Inputframe.pack(side = BOTTOM)

frame = Frame(root, width = 100, height = 10, bd = 5)
frame.pack()

ChatFrame = Frame(root, width = 100, height = 1000)
ChatFrame.pack(side = TOP)

ChatLabel = Label(ChatFrame, text="Welcome to the Chat Room!")
ChatLabel.pack()

textInput = Entry(Inputframe, width = 55, bd = 5)
textInput.pack(side = RIGHT)


scrollbar = Scrollbar(ChatFrame)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(ChatFrame, yscrollcommand = scrollbar.set, width = 80, height = 30 )

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

def buttonClicked():
    username = "default"
    message = textInput.get()
    mylist.insert(END, message)
    if mylist.get(1) != "":
        sendMessage = f"{username}: {message}"
        if message == "quit":
            s.close()
        s.send(sendMessage.encode('utf-8'))
    

button = Button(Inputframe, text="Send", width = 20, height = 2, bg = "gray83", command=buttonClicked)
button.pack(side = LEFT)

mylist.insert(END, "Enter your Username and click Send")

s = socket.socket()
host = "45.33.20.96"
port = 1234
s.connect((host, port))
def getMessages():
    while True:
        message = s.recv(1024).decode("utf-8")
        mylist.insert(END, f"\n{message}")

thread = Thread(target=getMessages)
thread.daemon = True
thread.start()

root.mainloop()
