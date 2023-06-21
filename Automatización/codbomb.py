import RPi.GPIO as GPIO
import time
from time import sleep

pump=int(input("Selecciona la bomba con la que vas a trabajar: "))
tiempo=int(input("ingrese el tiempo de operación de la bomba: "))
GPIO.setmode(GPIO.BCM)
GPIO.setup(pump,GPIO.OUT)


for i in range(1):
	GPIO.output(pump,0)
	print("Bomba trabajando")
	sleep(tiempo)
	GPIO.output(pump,1)
	print("Bomba apagada")
	sleep(3)
	
GPIO.cleanup()
