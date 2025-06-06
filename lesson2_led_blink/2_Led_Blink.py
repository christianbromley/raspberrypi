import RPi.GPIO as GPIO
import time

ledPin = 18  #define led pin

GPIO.setmode(GPIO.BCM)        # use BCM numbers
GPIO.setup(ledPin,GPIO.OUT)   #set the ledPin OUTPUT mode
GPIO.output(ledPin,GPIO.LOW)  # make ledPin output LOW level

# initialise count
n_blinks = 0
while n_blinks < 10:    #loop
    GPIO.output(ledPin,GPIO.HIGH)  #turn on led
    print("turned on the led")  #Print in the terminal
    time.sleep(5)              #wait for 1 second
    GPIO.output(ledPin,GPIO.LOW)   #turn off led
    print("turned off the led")
    time.sleep(2)
    n_blinks += 1

GPIO.cleanup()    #release all GPIO
