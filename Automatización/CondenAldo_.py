import RPi.GPIO as GPIO
import time
from time import sleep

pump1=13
pump2=22
pump3=27
pump4=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pump1,GPIO.OUT)
GPIO.setup(pump2,GPIO.OUT)
GPIO.setup(pump3,GPIO.OUT)
GPIO.setup(pump4,GPIO.OUT)

for i in range(1):
	print("INICIO DE LA REACCIÓN DE CONDENSACIÓN ALDÓLICA")
	GPIO.output(pump3,0)
	GPIO.output(pump2,1)
	GPIO.output(pump4,1)
	GPIO.output(pump1,1)
	print("Bomba 3 activada, añadiendo el hidroxido de sodio disuelto")
	sleep(24)
	GPIO.output(pump3,1)
	print("Desactivando bomba 3")
	sleep(2)
	GPIO.output(pump2,0)
	print("Bomba 2 activada, añadiendo la disolución de benzaldehido")
	sleep(25)
	GPIO.output(pump2,1)
	print("Desactivando bomba 2")
	sleep(2)
	GPIO.output(pump1,0)
	print("Enfriando la reacción")
	sleep(2)
	GPIO.setup(pump1,1)
	print("")
	sleep(30)
	GPIO.output(pump4,0)
	print("Bomba 4 activada, añadiendo la acetona")
	sleep(22)
	GPIO.output(pump4,1)
	print("Desactivando bomba 4")
	sleep(2)
	print("LA REACCIóN CONTINUA CON AGITANCIÓN POR 25 MIN")
	sleep(1500)
	print("")
	print("LA REACCIóN FINALIZÓ :)!")
GPIO.cleanup()
