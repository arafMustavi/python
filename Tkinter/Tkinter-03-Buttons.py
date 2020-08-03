from tkinter import *

root = Tk()


def myClick():
    myLabel1 = Label(root, text="Hello User!\nWelcome to medBOT")
    loginButton = Button(root, text="Log IN", padx=50, bg="#155244")
    myLabel1.pack()
    loginButton.pack()


welcomeButton = Button(root, text="Start Experience", command=myClick, fg="blue")
welcomeButton.pack()

root.mainloop()
