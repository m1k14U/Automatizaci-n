import RPi.GPIO as GPIO
import time 
from time import sleep

bomba_1=17
bomba_2=27
bomba_3=22
bomba_4=13

GPIO.setmode(GPIO.BCM)
GPIO.setup(bomba_1,GPIO.OUT)
GPIO.setup(bomba_2,GPIO.OUT)
GPIO.setup(bomba_3,GPIO.OUT)
GPIO.setup(bomba_4,GPIO.OUT)
 
for i in range(1):
	GPIO.output(bomba_3,0)
	GPIO.output(bomba_2,1)
	GPIO.output(bomba_4,1)
	print("activando bomba 3, añadiendo el hidorxido de sodio disuelto")
	sleep(30)
	GPIO.output(bomba_3,1)
	print("desactivando bomba 3")
	sleep(5)
	GPIO.output(bomba_2,0)
	print("activando bomba 2, añadiendo la disolución de benzaldehido")
	sleep(16.5)
	GPIO.output(bomba_2,1)
	print("desactivando bomba 2")
	sleep(20)
	GPIO.output(bomba_4,0)
	print("activando bomba 4, añadiendo la acetona")
	sleep(33.2)
	GPIO.output(bomba_4,1)
	print("desactivando bomba 4")
	sleep(5)
	
GPIO.cleanup()
