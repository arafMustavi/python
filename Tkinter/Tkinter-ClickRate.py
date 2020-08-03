# The goal of this module is to build a system that will find the click-rate of a user
# Update:
# The click Button Works but can't aggregate on the total number of clicks
from tkinter import *
import time

# start = time.time()
# # run your code
# end = time.time()
#
# elapsed = end - start



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


clickMe = Button(root, text="Click Me!", padx=50, command=clickCount)
stopButton = Button(root, text="Stop-Test", padx=50, command=myResult)

def initiateTest():
    global startTime
    startTime = time.time()
    clickMe.pack()
    stopButton.pack()


startButton = Button(root, text="Start-Test", padx=50, command=initiateTest)
startButton.pack()
root.mainloop()
