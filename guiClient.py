from tkinter import *

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


#textInput.insert(0,"Send something to the chat")
scrollbar = Scrollbar(ChatFrame)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(ChatFrame, yscrollcommand = scrollbar.set, width = 80, height = 30 )

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

def buttonClicked():
    message = textInput.get()
    mylist.insert(END, message)

button = Button(Inputframe, text="Send", width = 20, height = 2, bg = "gray83", command=buttonClicked)
button.pack(side = LEFT)

root.mainloop()