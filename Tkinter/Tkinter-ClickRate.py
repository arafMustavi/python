# The goal of this module is to build a system that will find the click-rate of a user
# Update:
# The Click rate works, Need to store the Data

from tkinter import *
import time
# Initiate the Roots and Frames
root = Tk()
total_Click = 0
startTime = 0


def clickCount():
    global total_Click
    total_Click += 1


def myResult():
    global total_Click
    endTime = time.time()
    elapsedTime = (endTime - startTime)
    clickRate = total_Click/elapsedTime
    clickRate = "{:.2f}".format(clickRate)
    # report_string = "Total Pressed : " + str(total_Click)
    # report_string += "\nWithin the time-frame :" + str(elapsedTime)
    report_string = "\nClick Rate :" + str(clickRate) + " Clicks per Second"
    report = Label(root, text=report_string)
    report.pack()
    exitButton.pack()


def initiateTest():
    global startTime
    startTime = time.time()
    clickMe.pack()
    stopButton.pack()

def endTest():
    root.quit()
    root.destroy()
    exit()


# Buttons Used in the frames
clickMe = Button(root, text="Click Me!", padx=50, command=clickCount)
stopButton = Button(root, text="Stop-Test", padx=50, command=myResult)
startButton = Button(root, text="Start-Test", padx=50, command=initiateTest)
exitButton = Button(root, text="Exit", padx=50, command=endTest)


# Initiate The Program
root.iconbitmap("icon.ico")
startButton.pack()


root.mainloop()
root.quit()