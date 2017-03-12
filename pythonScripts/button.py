# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import sys
import time

inputPin = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)

GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    if(GPIO.input(inputPin) == GPIO.LOW):
        print('Button is pressed')
        time.sleep(0.2)
