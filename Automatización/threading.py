import RPi.GPIO as GPIO
import time 
from time import sleep
import threading

GPIO.setmode(GPIO.BCM)

bomba_1=17
bomba_2=27
bomba_3=22
bomba_4=13

#bombas 
GPIO.setup(bomba_1,GPIO.OUT)
GPIO.setup(bomba_2,GPIO.OUT)
GPIO.setup(bomba_3,GPIO.OUT)
GPIO.setup(bomba_4,GPIO.OUT)

def Pump_1():
	GPIO.output(13,0)
	print('Activando Bomba_1 \n')
	sleep(2)
	GPIO.output(13,1)
	print('Desactivando la Bomba_1 \n')
	sleep(1)
def Pump_2():
	GPIO.output(22,0)
	print('Activando Bomba_2 \n')
	sleep(2)
	GPIO.output(22,1)
	print('Desactivando la Bomba_2 \n')
	sleep(1)
def Pump_3():
	GPIO.output(27,1)
	print('Activando Bomba_3 \n')
	sleep(2)
	GPIO.output(27,0)
	print('Activando Bomba_3 \n')
	sleep(1)
def Pump_4():
	GPIO.output(17,0)
	print('Activando Bomba_3 \n')
	sleep(2)
	GPIO.output(17,1)
	print('Desactivando la Bomba_3 \n')
	sleep(1)

h1=threading.Thread(target=Pump_1)
h2=threading.Thread(target=Pump_2)
h3=threading.Thread(target=Pump_3)
h4=threading.Thread(target=Pump_4)



h3.run()
h2.run()
h4.run()
h1.run()

GPIO.cleanup()
