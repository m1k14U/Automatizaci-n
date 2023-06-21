import RPi.GPIO as GPIO
import time
from time import sleep
from tkinter import *

def validate_integer(text):
    if text.isdigit() or text == "":
        return True
    else:
        return False

root = Tk()
root.title("Bombas para la Rxn")
root.geometry("1000x300")
pump=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(pump,GPIO.OUT)
validation= root.register(validate_integer)

bomba1 = Canvas(root, height=200, width=200)
bomba1.grid(row=1, column=0, columnspan=1,ipadx=20)


pump1label=Label(text="Bomba 1, Agua",bg='#6AADBF',font=("Cambria",13)).grid(row=0, column=0, columnspan=1)

pump1=bomba1.create_oval(50,10,200,160, fill="", outline="black")


c1 = bomba1.create_oval(121, 80, 131, 90, fill="black", outline="")
tube1_1 = bomba1.create_rectangle(100, 155, 105, 200, fill="white", outline="black")
tube2_1 = bomba1.create_rectangle(145, 155, 150, 200, fill="white", outline="black")



tiempo1=Entry(root)
tiempo1.grid(row=2, column=0, columnspan=1)

def Bomba1():
    tiempo=tiempo1.get()
    if tiempo.isdigit():
        tim=sum(int(digit)* 10 ** i for i, digit in enumerate(tiempo[::-1]))
        #print(type(tim))
        pump=13
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pump,GPIO.OUT)

        GPIO.output(pump,0)
        print("Bomba activada")
        sleep(tim)
        GPIO.output(pump,1)
        print("Bomba apagada")
        sleep(2)

    else:
        print("Invalid")
    

btn1 = Button(root, text="Aplicar",command=Bomba1).grid(row=3, column=0, columnspan=1)

Bomba1()
GPIO.cleanup()
mainloop()
