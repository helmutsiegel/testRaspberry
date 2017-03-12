import RPi.GPIO as GPIO
import sys
import time

inputPin = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)

GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print GPIO.input(inputPin)
