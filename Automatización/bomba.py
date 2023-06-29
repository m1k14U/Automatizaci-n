import RPi.GPIO as GPIO
import time
from time import sleep
from tkinter import *

pump=int(input("Ingrese el pin de la bomba que quiere utilizar: "))
ventana=Tk()
ventana.title("Controlador de una bomba")
ventana.geometry("350x350")

pump1= Canvas(ventana, height=300, width=250)
pump1.grid(row=1, column=0, ipadx=60,ipady=1)

pumplabel_1=Label(text="Bomba", bg='grey', font=("Arial",20))
pumplabel_1.place(x=130,y=10)

bomba=pump1.create_oval(90,50, 260, 220, fill="green", outline="black")
c1=pump1.create_oval(170, 130, 180, 140, fill="grey", outline="")
tube1_1 = pump1.create_rectangle(125, 200, 135, 250, fill="white", outline="black")
tube2_1 = pump1.create_rectangle(210, 200, 220, 250, fill="white", outline="black")

def encendido():
    bomba=pump
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(bomba,GPIO.OUT)
    
    GPIO.output(bomba,0)
    print("Bomba encendida")
    
def apagado():
    bomba=pump
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(bomba,GPIO.OUT)
    
    GPIO.output(bomba,1)
    print("Bomba apagada")
    
btton=Button(ventana, text="ON",command=encendido).place(x=150,y=250)
btton=Button(ventana, text="OFF",command=apagado).place(x=147,y=280)

encendido()
apagado()
mainloop()
GPIO.cleanup()
