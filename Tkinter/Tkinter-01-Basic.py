from tkinter import *
# Everything in tkinter is a widget
# We start with the Root Widget

root = Tk()
# Creating a Label Widget
myLabel = Label(root, text="Hello Araf Mustavi!")
# Shoving it onto the screen
myLabel.pack()
# Pack floats around the window
root.mainloop()
