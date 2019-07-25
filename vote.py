from gpiozero import LED,Button
from interface import *

import tkinter as tk
#from tkinter import *
root = tk.Tk()
app = tk.Frame(root)
app.pack()
root.geometry("1200x1200")
root.title("ELECTRONIC VOTING MACHINE")
electoralLabel = tk.Label(app, text="ELECTORAL COMMISSION OF GHANA \n HO TECHNICAL UNIVERSITY SRC ELECTIONS", fg="blue", font="Times 40" )
copyrightLabel = tk.Label(app, text="@CopyRight|TeamCoded", font="Times 20")
electoralLabel.pack(pady = 20)

#def addvote1():
#    led1.on()
#    button1.when_released = led1.off
#    countVote1.set(1 + countVote1.get())
#    label1['text'] = "BENEDICTA final resultS = " + str(countVote1.get())
#    label1['font'] = '60'
#    print ("\tBENEDICTA final resultS = ", countVote1.get())

l_candidates = setupMachine()
l_labels = []
l_counts = []
l_buttons = []
l_leds = []

#led_pins = [18, 23, 22]
#button_pins = [6, 12, 13]
#fg_cols = ["white", "black", "white"]
#bg_cols = ["red", "green", "blue"]


# for loop over l_candidates...

button1 = Button(6)
led1 = LED(18)
countVote1 = tk.IntVar()
countVote1.set(0)
label1 = tk.Label(app, fg="white", bg="red")
label1.pack(fill = tk.X, pady=30)

button2 = Button(12)
led2 = LED(23)
countVote2 = tk.IntVar()
countVote2.set(0)
label2 = tk.Label(app, fg="black",bg="green")
label2.pack(fill = tk.X, pady=30)


button3 = Button(13)
led3 = LED(22)
countVote3 = tk.IntVar()
countVote3.set(0)
label3 = tk.Label(app, fg="white",bg="blue" )
label3.pack(fill= tk.X, pady=30)


copyrightLabel.pack(pady=145)

l_labels = [label1, label2, label3]
l_counts = [countVote1, countVote2, countVote3]
l_buttons = [button1, button2, button3]
l_leds = [led1, led2, led3]

l_callbacks = position_callback_maker(l_candidates, l_labels, l_counts, l_buttons, l_leds)

print("ELECTORAL COMMISSION OF GHANA")
print("HO TECHNICAL SRC ELECTION RESULT")
button1.when_pressed = l_callbacks[0]
button2.when_pressed = l_callbacks[1]
button3.when_pressed = l_callbacks[2]

root.mainloop()