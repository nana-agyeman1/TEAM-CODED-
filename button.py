import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(19)
    if input_state == False:
        print('successfully')
        time.sleep(3)
   # else:
    #    print('button pressed')
     #   time.sleep(2)
        


