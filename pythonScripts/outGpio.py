import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False);

ledPin = int(sys.argv[1])

GPIO.setmode(GPIO.BCM) 
GPIO.setup(ledPin, GPIO.OUT)
if int(sys.argv[2]) == 0 :
    GPIO.output(ledPin, GPIO.LOW)
else :
    GPIO.output(ledPin, GPIO.HIGH)
    

