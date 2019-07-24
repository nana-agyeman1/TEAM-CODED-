from gpiozero import LED,Button
#from time import sleep
from tkinter import *
root = Tk()
app = Frame(root)
app.grid()
root.geometry("500x250")
root.title("ELECTRONIC VOTING MACHINE")


button1 = Button(6)
button2 = Button(12)
button3 = Button(13)

led1 = LED(18)
led3 = LED(22)
led2 = LED(23)

countVote1 = 0
countVote2 = 0
countVote3 = 0

def addvote1():
    global countVote1
    led1.on()
    button1.when_released = led1.off
    countVote1 += 1
    print (" 1 final result = ")

def addvote2():
    global countVote2
    led2.on()
    button2.when_released = led2.off
    countVote2 += 1
    print (" 2 final result = ")

def addvote3():
    global countVote3
    led3.on()
    button3.when_released = led3.off
    countVote3 += 1
    print ( " 3 final result = ") 


button1.when_pressed = addvote1
button2.when_pressed = addvote2
button3.when_pressed = addvote3

l1 = Label(app, text="ELECTRAL COMMISSION", font = 50)
l2 = Label(app, text="HO TECHNICAL UNIVERSITY ELECTIONS 2019", font = 50)
l3 = Label(app, text="ELECTRAL COMMISSION", font = 50)
l4 = Label(app, text="CANDIDATE : " + int(countVote1))
l5 = Label(app, text="CANDIDATE : " + int(countVote2))
l6 = Label(app, text="CANDIDATE : " + int(countVote3))
l1.grid(row = 0, column = 2, sticky = W)
l2.grid(row = 1, column = 2, sticky = W)
l4.grid(row = 2, column = 1, sticky = W)
l5.grid(row = 3, column = 1, sticky = W)
l6.grid(row = 4, column = 1, sticky = W)
root.mainloop()

