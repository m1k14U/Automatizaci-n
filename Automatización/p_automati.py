impo rt RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

motor_A=
motor_B=
bomba_1=17
bomba_2=27
bomba_3=22
bomba_4=13

#bombas
GPIO.setup(bomba_1,GPIO.OUT)
GPIO.setup(bomba_2,GPIO.OUT)
GPIO.setup(bomba_3,GPIO.OUT)
GPIO.setup(bomba_4,GPIO.OUT)

#motores A y B
GPIO.setup(motor_A,GPIO.OUT)
GPIO.setup(motor_B,GPIO.OUT)
#direcciones motor A
GPIO.setup(,GPIO.OUT)
GPIO.setup(,GPIO.OUT)
#direcciones motor B
GPIO.setup(,GPIO.OUT)
GPIO.setup(,GPIO.OUT)
#frecuencia para los motores
pw_A=GPIO.PWM(motor_A,500)
pw_B=GPIO.PWM(motor_B,500)

pw_A.start(0)
pw_B.start(0)

def Dir_Fav_Reloj_motorA():
	GPIO.output(,0)
	GPIO.output(,1)
def Dir_Cont_Reloj_motorA():
	GPIO.output(,1)
	GPIO.output(,0)
def Dir_Fav_Reloj_motorB():
	GPIO.output(,0)
	GPIO.output(,1)
def Dir_Cont_Reloj_motorB():
	GPIO.output(,1)
	GPIO.output(,0)

print('-Elegir el motor A o B  \n -Elegir dirección F o C \n -Elegir velocidad 0 a 100')
print("ejemplo 'AF50' (motor, dirección, velocidad)")
print('presionar Ctrl+C para salir')

try:
	while True:
		cmd = raw_input('insertar el comando')
		cmd = cmd.lower()
		motor = cmd[0]
		velocidad = cmd[2:5]

		if motor == 'A':
			if direccion == 'f':
				Dir_Fav_Reloj_motorA()
				print('motor A, Reloj, vel='+velocidad)
			elif direccion == 'r':
				Dir_Cont_Reloj_motorA()
				print('motor A, Contra reloj, vel='+velocidad)
			else 
				print('No estas seleccionando una dirección posible')
			pw_A.ChangeDutyCycle(int(velocidad))
		elif motor == 'B':
			if direccion == 'f':
				Dir_Fav_Reloj_motorB()
				print('motor B, Reloj, vel='+velocidad)
			elif direccion == 'r':
				Dir_Cont_Reloj_motorB()
				print('motor B, Contra reloj, vel='+velocidad)
			else 
				print('No estas seleccionando una dirección posible')
			pw_B.ChangeDutyCycle(int(velocidad))
		else
		print('no estas seleccionando el motor A o B')

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
	
except KeyboardInterrupt:
	pw_A.stop()
	pw_B.stop()
	GPIO.cleanup()
	exit()
