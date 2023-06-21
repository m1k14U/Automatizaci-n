from tkinter import *

root = Tk()
root.title("Bombas para la Rxn")
root.geometry("1000x300")

bomba1 = Canvas(root, height=200, width=200)
bomba1.grid(row=1, column=0, columnspan=1,ipadx=20)
bomba2 = Canvas(root, height=200, width=200)
bomba2.grid(row=1, column=1, columnspan=1, ipadx=20)
bomba3 = Canvas(root, height=200, width=200)
bomba3.grid(row=1, column=2, columnspan=1, ipadx=20)
bomba4 = Canvas(root, height=200, width=200)
bomba4.grid(row=1, column=3, columnspan=1, ipadx=20)

pump1label=Label(text="Bomba 1, Agua",bg='#6AADBF',font=("Cambria",13)).grid(row=0, column=0, columnspan=1)
pump2label=Label(text="Bomba 2",bg='#6AADBF',font=("Cambria",13)).grid(row=0, column=1, columnspan=1)
pump3label=Label(text="Bomba 3",bg='#6AADBF',font=("Cambria",13)).grid(row=0, column=2, columnspan=1)
pump4label=Label(text="Bomba 4",bg='#6AADBF',font=("Cambria",13)).grid(row=0, column=3, columnspan=1)

pump1=bomba1.create_oval(50,10,200,160, fill="", outline="black")
pump2=bomba2.create_oval(50,10,200,160, fill="green", outline="black")
pump3=bomba3.create_oval(50,10,200,160, fill="green", outline="black")
pump4=bomba4.create_oval(50,10,200,160, fill="green", outline="black")

c1 = bomba1.create_oval(121, 80, 131, 90, fill="black", outline="")
c2 = bomba2.create_oval(121, 80, 131, 90, fill="black", outline="")
c3 = bomba3.create_oval(121, 80, 131, 90, fill="black", outline="")
c4 = bomba4.create_oval(121, 80, 131, 90, fill="black", outline="")

tube1_1 = bomba1.create_rectangle(100, 155, 105, 200, fill="white", outline="black")
tube2_1 = bomba1.create_rectangle(145, 155, 150, 200, fill="white", outline="black")
tube1_2 = bomba2.create_rectangle(100, 155, 105, 200, fill="white", outline="black")
tube2_2 = bomba2.create_rectangle(145, 155, 150, 200, fill="white", outline="black")
tube1_3 = bomba3.create_rectangle(100, 155, 105, 200, fill="white", outline="black")
tube2_3 = bomba3.create_rectangle(145, 155, 150, 200, fill="white", outline="black")
tube1_4 = bomba4.create_rectangle(100, 155, 105, 200, fill="white", outline="black")
tube2_4 = bomba4.create_rectangle(145, 155, 150, 200, fill="white", outline="black")

tiempo1=Entry().grid(row=2, column=0, columnspan=1)
tiempo2=Entry().grid(row=2, column=1, columnspan=1)
tiempo3=Entry().grid(row=2, column=2, columnspan=1)
tiempo4=Entry().grid(row=2, column=3, columnspan=1)

btn1 = Button(root, text="Aplicar").grid(row=3, column=0, columnspan=1)
btn2 = Button(root, text="Aplicar").grid(row=3, column=1, columnspan=1)
btn3 = Button(root, text="Aplicar").grid(row=3, column=2, columnspan=1)
btn4 = Button(root, text="Aplicar").grid(row=3, column=3, columnspan=1)

mainloop()
