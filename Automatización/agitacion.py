import RPi.GPIO as GPIO
from time import sleep 
GPIO.setmode(GPIO.BCM)

motorA_1= 20 
motorB_1= 24 

GPIO.setup(motorA_1, GPIO.OUT) 
GPIO.setup(motorB_1, GPIO.OUT) 

def MOVERMOTOR(x):
	if x==0:
		GPIO.output(motorA_1,1)
		GPIO.output(motorB_1,0)
	elif x==0:
		GPIO.output(motorB_1,1)
		GPIO.output(motorA_1,0)
	else:
		GPIO.output(motorB_1,0)
		GPIO.output(motorA_1,0)
try:
	while True:
		MOVERMOTOR()
		sleep()

except KeyboardInterrupt:
	GPIO.cleanup()



