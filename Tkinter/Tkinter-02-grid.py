from tkinter import *

# Everything in tkinter is a widget
# We start with the Root Widget

root = Tk()
# Creating a Label Widget
myLabel1 = Label(root, text="Hello User!")
myLabel2 = Label(root, text="Welcome to medBOT")

# Put labels onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
# Grid assigns the texts exacts in the position
# Grid creates a relative position

root.mainloop()
