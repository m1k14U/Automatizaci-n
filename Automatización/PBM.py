import RPi.GPIO as GPIO
import time 
from time import sleep
import threading

GPIO.setmode(GPIO.BCM)

bomba_1=17
bomba_2=27
bomba_3=22
bomba_4=13

motor_A=24
motor_A1=12
motor_A2=20

#bombas 
GPIO.setup(bomba_1,GPIO.OUT)
GPIO.setup(bomba_2,GPIO.OUT)
GPIO.setup(bomba_3,GPIO.OUT)
GPIO.setup(bomba_4,GPIO.OUT)
#servomotor
GPIO.setup(motor_A,GPIO.OUT)
GPIO.setup(motor_A1,GPIO.OUT)
GPIO.setup(motor_A2,GPIO.OUT)
pw_A=GPIO.PWM(motor_A,500)
pw_A.start(0)

def Dir_Fav_Reloj_motorA():
	GPIO.outout(12,0)
	GPIO.output(20,0)
	sleep(15)
	GPIO.output(12,0)
	print('Activando motor \n')
	GPIO.output(20,1)
	pw_A.ChangeDutyCycle(80)
	sleep(10)
	print('Desactivando motor \n')

def Dir_Contr_Reloj_motorA():
	GPIO.outout(12,0)
	GPIO.output(20,0)
	sleep(30)
	GPIO.output(12,1)
	print('Activando motor \n')
	GPIO.output(20,0)
	pw_A.ChangeDutyCycle(80)
	sleep(15)
	print('Desactivando motor \n')	
	
def Pump_1():
	GPIO.output(13,1)
	sleep(80)
	GPIO.output(13,0)
	print('Activando Bomba_1 \n')
	sleep(20)
	GPIO.output(13,1)
	print('Desactivando la Bomba_1 \n')
	sleep(5)
def Pump_2():
	GPIO.output(22,1)
	sleep(30)
	GPIO.output(22,0)
	print('Activando Bomba_2 \n')
	sleep(16.5)
	GPIO.output(22,1)
	print('Desactivando la Bomba_2 \n')
	sleep(5)
def Pump_3():
	GPIO.output(27,1)
	print('Activando Bomba_3 \n')
	sleep(30)
	GPIO.output(27,0)
	print('Activando Bomba_3 \n')
	sleep(5)
def Pump_4():
	GPIO.output(17,1)
	sleep(46.5)
	GPIO.output(17,0)
	print('Activando Bomba_3 \n')
	sleep(33.2)
	GPIO.output(17,1)
	print('Desactivando la Bomba_3 \n')
	sleep(5)
	

h1=threading.Thread(target=Pump_1)
h2=threading.Thread(target=Pump_2)
h3=threading.Thread(target=Pump_3)
h4=threading.Thread(target=Pump_4)
hm=threading.Thread(target=Dir_Fav_MotorA)
hm2=threading.Thread(target=Dir_Contr_MotorA)


h3.start()
hm.start()
h2.start()
h4.start()
h1.start()
hm2.start()

pw_A.stop()
GPIO.cleanup_()
