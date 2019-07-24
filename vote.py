from gpiozero import LED,Button



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
    print (" BENEDICTA final resultS = ", countVote1)

def addvote2():
    global countVote2
    led2.on()
    button2.when_released = led2.off
    countVote2 += 1
    print (" BRIDGET final resultS = ", countVote2)

def addvote3():
    global countVote3
    led3.on()
    button3.when_released = led3.off
    countVote3 += 1
    print ( " ALEX final resultS = ", countVote3) 

print("ELECTORAL COMMISSION OF GHANA")
print("HO TECHNICAL SRC ELECTIONS RESULT")
button1.when_pressed = addvote1
button2.when_pressed = addvote2
button3.when_pressed = addvote3


