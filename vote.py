from gpiozero import LED,Button

import tkinter as tk

root = tk.Tk()
app = tk.Frame(root)
app.pack()

button1 = Button(6)
button2 = Button(12)
button3 = Button(13)

led1 = LED(18)
led3 = LED(22)
led2 = LED(23)

countVote1 = tk.IntVar()
countVote1.set(0)
countVote2 = tk.IntVar()
countVote2.set(0)
countVote3 = tk.IntVar()
countVote3.set(0)


label1 = tk.Label(app, fg="green")
label1.pack()

#label = tk.Label(root, fg="green")
#label.pack()
#counter_label(label)
#button = tk.Button(root, text='Stop', width=25, command=root.destroy)
#button.pack()



def addvote1():
    led1.on()
    button1.when_released = led1.off
    countVote1.set(1 + countVote1.get())
    label1['text'] = "BENEDICTA final resultS = " + str(countVote1.get())
    print ("\tBENEDICTA final resultS = ", countVote1.get(),"\n")

def addvote2():
    led2.on()
    button2.when_released = led2.off
    countVote2.set(1 + countVote2.get())    
    print ("\tBRIDGET final resultS = ", countVote2.get(),"\n")

def addvote3():
    led3.on()
    button3.when_released = led3.off
    countVote3.set(1 + countVote3.get())
    print ( "\tALEX final resultS = ", countVote3.get(),"\n") 

print("ELECTORAL COMMISSION OF GHANA")
print("HO TECHNICAL SRC ELECTION RESULT")
button1.when_pressed = addvote1
button2.when_pressed = addvote2
button3.when_pressed = addvote3


tkB = tk.Button(app, command=countVote1)
tkB.pack()
root.mainloop()