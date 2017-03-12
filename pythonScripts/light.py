 
import RPi.GPIO as GPIO
import time
import sys


RCpin = int(sys.argv[1]);
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RCpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i = 0
while i < 10:
        i = i+1
        print GPIO.input(RCpin)
        time.sleep(0.5)

GPIO.cleanup()
