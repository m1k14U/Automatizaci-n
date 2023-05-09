from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Bombas para la Rxn")
ventana = Canvas(root, bg="#D2D9C0",
            height=350, width=850)

tiempo1=ttk.Entry(int())
tiempo1.place(x=60,y=280)
tiempo2=ttk.Entry()
tiempo2.place(x=260,y=280)
tiempo3=ttk.Entry(int())
tiempo3.place(x=460,y=280)
tiempo4=ttk.Entry(int())
tiempo4.place(x=660,y=280)


pump1=ventana.create_oval(50,40,200,
                         190,
                         outline="black")
c1=ventana.create_oval(120,110,130,
                         120,
                         fill="silver", outline="black")
pump2=ventana.create_oval(250,40,400,
                         190,
                         fill="green", outline="black")
c2=ventana.create_oval(320,110,330,
                         120,
                         fill="silver", outline="")
pump3=ventana.create_oval(450,40,600,
                         190,
                         fill="green", outline="black")
c3=ventana.create_oval(520,110,530,
                         120,
                         fill="silver", outline="")
pump4=ventana.create_oval(650,40,800,
                         190,
                         fill="green", outline="black")
c4=ventana.create_oval(720,110,730,
                         120,
                         fill="silver", outline="")
tube1_1=ventana.create_rectangle(100,188,105,
                         250,
                         fill="white", outline="")
tube2_1=ventana.create_rectangle(145,188,150,
                         250,
                         fill="white", outline="")
tube1_2=ventana.create_rectangle(300,188,305,
                         250,
                         fill="white", outline="")
tube2_2=ventana.create_rectangle(345,188,350,
                         250,
                         fill="white", outline="")
tube1_3=ventana.create_rectangle(500,188,505,
                         250,
                         fill="white", outline="")
tube2_3=ventana.create_rectangle(545,188,550,
                         250,
                         fill="white", outline="")
tube1_4=ventana.create_rectangle(700,188,705,
                         250,
                         fill="white", outline="")
tube2_4=ventana.create_rectangle(745,188,750,
                         250,
                         fill="white", outline="")
pump1_label=Label(text="Bomba 1",bg='#6AADBF',font=("Cambria",13))
pump1_label.place(x=90,y=8)
pump2_label=Label(text="Bomba 2",bg='#6AADBF',font=("Cambria",13))
pump2_label.place(x=290,y=8)
pump3_label=Label(text="Bomba 3",bg='#6AADBF',font=("Cambria",13))
pump3_label.place(x=490,y=8)
pump4_label=Label(text="Bomba 4",bg='#6AADBF',font=("Cambria",13))
pump4_label.place(x=690,y=8)

Button(root, text="Iniciar").place(x=405,y=320)


ventana.pack()
mainloop()
