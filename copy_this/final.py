import RPi.GPIO as GPIO
from gpiozero import LED
import time
from tkinter import *
root = Tk()
app = Frame(root)
root.geometry("500x250")
l1 = Label(app, text="ELECTRAL COMMISSION", font = 50)
l2 = Label(app, text="HO TECHNICAL UNIVERSITY ELECTIONS 2019", font = 50)
l1 = Label(app, text="ELECTRAL COMMISSION", font = 50)
state = 0
no_of_pos = 0
pos = {}
light1 =18
light2 = 22
light3 = 23
start_button = 4
result_button = 20
button1 = 6
button2 = 12
button3 = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(light1,GPIO.OUT)
GPIO.setup(light2,GPIO.OUT)
GPIO.setup(light3,GPIO.OUT)
GPIO.setup(start_button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(result_button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def showLight(st):    
    if st == 0:
        GPIO.output(light1,GPIO.LOW)
        GPIO.output(light2,GPIO.LOW)
        GPIO.output(light3,GPIO.LOW)
        
    elif st == 1:
        GPIO.output(light1,GPIO.HIGH)
        GPIO.output(light2,GPIO.HIGH)
        GPIO.output(light3,GPIO.HIGH)
        

def setupMachine():
    global state

    no_of_pos = int(raw_input("Enter no. of positions:")) 
    for i in range(no_of_pos):
        name = raw_input("Enter position name (max 12 char long):")
        can = int(raw_input("Enter no. of candidates:"))
        can_list = {}
        for j in range(can):
            can_name = raw_input("Enter name of candidate no. " + str(j + 1) + ":")
            can_list[j] = can_name
        pos[name] = can_list    
    state = 1
    print(state)
    print("Setup successful")
 
def startForOnePerson(self):
    print ("starting...")
    self.setText("Starting...")
    time.sleep (1)
    
    for pos_name, can_list in pos.iteritems():
        #print position name in first row
        line1 = ""
        line2 = ""
        line3 = ""
        
        line1 += pos_name        
        #print candidates in second row
        for can in can_list.keys():
            line2 += can + " "
        self.setText(line1 + "\n" + line2 + "\n" + line3)
        time.sleep(0.5)

        showLight(1)
        while True:
            input1 = GPIO.input(button1)
            input2 = GPIO.input(button2)
            input3 = GPIO.input(button3)

            if input1 == False:
                pos[pos_name][can_list.keys()[0]] += 1
                line1 += "  " + can_list.keys()[0]
                time.sleep(2)
                print("vote to 1")
                break
            elif input2 == False:
                pos[pos_name][can_list.keys()[1]] += 1
                line1 += "  " + can_list.keys()[1]
                time.sleep(2)
                print("vote to 2")
        setText(line1 + "\n" + line2)
        showLight(0)        
        time.sleep(2)        
    print ("vote recorded")

def printResult():
    print ("Showing result:")

    line1 = "Showing result"    
    for pos_name, can_list in pos.iteritems():
        mx = -1
        line2 = ""
        for x , y in can_list.iteritems():
            if y > mx:
                mx=y
        for x , y in can_list.iteritems():
            if y == mx:
                line2 += x + " "
        setText(line1 + "\n" + line2)
        time.sleep(3)
                
def startMachine():
    global state
    while True:
        start = GPIO.input(start_button)
        res = GPIO.input(result_button)
        if start == False:
            time.sleep(2)
            if state == 0:        
                setupMachine()
                print(state)
            elif state == 1:
                startForOnePerson(self)
            
        elif res == False:
            time.sleep(2)
            printResult()
            break
               
    
    

setupMachine()
startMachine()
