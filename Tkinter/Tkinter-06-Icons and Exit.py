from tkinter import *

root = Tk()
root.title("medBOT")

# Icon is a ico file
root.iconbitmap("icon.ico")

# quitButton = Button(root, text="Quit", padx=50, command=root.quit).pack()

exitButton = Button(root, text="Exit", padx=50, command=root.destroy)
exitButton.pack()

root.mainloop()
