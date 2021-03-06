import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledPin = 4 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
print("Here we go! Press CTRL+C to exit")
try:
    while 1:
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.35)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.35)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
