from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO


pump1=13
pump2=22
pump3=27
pump4=17
pump5=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pump1,GPIO.OUT)
GPIO.setup(pump2,GPIO.OUT)
GPIO.setup(pump3,GPIO.OUT)
GPIO.setup(pump4,GPIO.OUT)
GPIO.setup(pump5,GPIO.OUT)


root = Tk()
root.title("MIK-I")
ventana = Canvas(root, bg="white",
            height=650, width=1200)


pump1=ventana.create_oval(50,40,200,190,outline="black")
c1=ventana.create_oval(120,110,130,120,fill="silver", outline="black")
pump2=ventana.create_oval(250,40,400,190,fill="green", outline="black")
c2=ventana.create_oval(320,110,330,120,fill="silver", outline="")
pump3=ventana.create_oval(450,40,600,190,fill="green", outline="black")
c3=ventana.create_oval(520,110,530,120,fill="silver", outline="")
pump4=ventana.create_oval(650,40,800,190,fill="green", outline="black")
c4=ventana.create_oval(720,110,730,120,fill="silver", outline="")
pump5=ventana.create_oval(850,40,1000,190,fill="green", outline="black")
c5=ventana.create_oval(920,110,930,120,fill="silver", outline="")
pump6=ventana.create_oval(150,350,300,500,fill="green", outline="black")
c6=ventana.create_oval(220,420,230,430,fill="silver", outline="")
pump7=ventana.create_oval(350,350,500,500,fill="green", outline="black")
c7=ventana.create_oval(420,420,430,430,fill="silver", outline="")
pump8=ventana.create_oval(550,350,700,500,fill="green", outline="black")
c8=ventana.create_oval(620,420,630,430,fill="silver", outline="")
pump9=ventana.create_oval(750,350,900,500,fill="green", outline="black")
c9=ventana.create_oval(820,420,830,430,fill="silver", outline="")
pump10=ventana.create_oval(950,350,1100,500,fill="green", outline="black")
c10=ventana.create_oval(1020,420,1030,430,fill="silver", outline="")



pump1_label=Label(text="Bomba 1",bg='white',font=("Cambria",13))
pump1_label.place(x=90,y=8)
pump2_label=Label(text="Bomba 5",bg='white',font=("Cambria",13))
pump2_label.place(x=290,y=8)
pump3_label=Label(text="Bomba 2",bg='white',font=("Cambria",13))
pump3_label.place(x=490,y=8)
pump4_label=Label(text="Bomba 3",bg='white',font=("Cambria",13))
pump4_label.place(x=690,y=8)
pump5_label=Label(text="Bomba 4",bg='white',font=("Cambria",13))
pump5_label.place(x=890,y=8)
pump6_label=Label(text="Bomba 6",bg='white',font=("Cambria",13))
pump6_label.place(x=190,y=320)
pump7_label=Label(text="Bomba 7",bg='white',font=("Cambria",13))
pump7_label.place(x=390,y=320)
pump8_label=Label(text="Bomba 8",bg='white',font=("Cambria",13))
pump8_label.place(x=590,y=320)
pump9_label=Label(text="Bomba 9",bg='white',font=("Cambria",13))
pump9_label.place(x=790,y=320)
pump10_label=Label(text="Bomba 10",bg='white',font=("Cambria",13))
pump10_label.place(x=990,y=320)


Button(root, text="ON",command="bomba1ON").place(x=100,y=200)
Button(root, text="ON",command="bomba2ON").place(x=300,y=200)
Button(root, text="ON",command="bomba3ON").place(x=500,y=200)
Button(root, text="ON",command="bomba4ON").place(x=700,y=200)
Button(root, text="ON",command="bomba5ON").place(x=900,y=200)
Button(root, text="ON",command="").place(x=200,y=510)
Button(root, text="ON",command="").place(x=400,y=510)
Button(root, text="ON",command="").place(x=600,y=510)
Button(root, text="ON",command="").place(x=800,y=510)
Button(root, text="ON",command="").place(x=1000,y=510)

Button(root, text="OFF",command="bomba1OFF").place(x=98,y=240)
Button(root, text="OFF",command="bomba2OFF").place(x=298,y=240)
Button(root, text="OFF",command="bomba3OFF").place(x=498,y=240)
Button(root, text="OFF",command="bomba4OFF").place(x=698,y=240)
Button(root, text="OFF",command="bomba5OFF").place(x=898,y=240)
Button(root, text="OFF",command="").place(x=198,y=550)
Button(root, text="OFF",command="").place(x=398,y=550)
Button(root, text="OFF",command="").place(x=598,y=550)
Button(root, text="OFF",command="").place(x=798,y=550)
Button(root, text="OFF",command="").place(x=998,y=550)

def bomba1ON():
    GPIO.output(pump1,0)
    print("Bomba 1 trabajando")

def bomba2ON():
    GPIO.output(pump2,0)
    print("Bomba 2 trabajando")

def bomba3ON():
    GPIO.output(pump3,0)
    print("Bomba 3 trabajando")

def bomba4ON():
    GPIO.output(pump4,0)
    print("Bomba 4 trabajando")

def bomba5ON():
    GPIO.output(pump5,0)
    print("Bomba 5 trabajando")




def bomba1OFF():
    GPIO.output(pump1,1)
    print("Bomba 1 apagada")

def bomba2OFF():
    GPIO.output(pump2,1)
    print("Bomba 2 apagada")

def bomba3OFF():
    GPIO.output(pump3,1)
    print("Bomba 3 apagada")

def bomba4OFF():
    GPIO.output(pump4,1)
    print("Bomba 4 apagada")

def bomba5OFF():
    GPIO.output(pump5,1)
    print("Bomba 5 apagada")


ventana.pack()
mainloop()
