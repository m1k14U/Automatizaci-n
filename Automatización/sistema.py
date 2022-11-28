import RPi.GPIO as GPIO
import time 
from time import sleep
import threading

GPIO.setmode(GPIO.BCM)
motor_A=24
#bombas 
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
#servomotor
GPIO.setup(motor_A,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
pw_A=GPIO.PWM(motor_A,500)
pw_A.start(0)

def Dir_Fav_Reloj_motorA():
	GPIO.output(20,0)
	pw_A.ChangeDutyCycle(80)
	sleep(10)
	GPIO.output(21,1)
	
def Pump_1():
	GPIO.output(13,0)
	sleep(10)
	GPIO.output(13,1)
def Pump_2():
	GPIO.output(22,0)
	sleep(5)
	GPIO.output(22,1)
def Pump_3():
	GPIO.output(27,0)
	sleep(5)
	GPIO.output(27,1)
def Pump_4():
	GPIO.output(17,0)
	sleep(5)
	GPIO.output(17,1)
	

threading.Thread(target=Pump_1).start()
threading.Thread(target=Dir_Fav_Reloj_motorA).start()
