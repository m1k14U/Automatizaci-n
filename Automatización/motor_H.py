import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

for i in range(1):
	GPIO.output(17,0)
	GPIO.output(27,1)




GPIO.cleanup()