from tkinter import *


root = Tk()


# Show Username Insert Instruction
label1 = Label(root, text="Enter Username")
label1.pack()

# Data Insertion

e = Entry(root, width=50, bg="grey")
e.pack()
# e.insert(0, "User name:")
def action_click():
    message = "Hello "+ e.get() + "! Welcome Abroad!"
    label = Label(root, text=message)
    label.pack()


button1 = Button(root, text="Login", command=action_click)
button1.pack()
root.mainloop()
