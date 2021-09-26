from tkinter import*

window = Tk()
window.title("BMI Calculator")
def BMI():
    weight=float(e2.get())
    height=float(e2.get())
    bmi=(weight)/(height**2)
    t1.delete("1.0",END)
    t1.insert(END,height)
    t2.delete("1.0", END)
    t2.insert(END,weight)
    t3.delete("1.0", END)
    t3.insert(END,bmi)

e1=Label(window,text="Enter weight in kg:")
e2 = StringVar()
e2=Entry(window,textvariable = e2)
e3=Label(window,text="Enter the height in meter:")
e4 = StringVar()
e4=Entry(window,textvariable = e4)
e5 = Label(window, text = 'BMI:')

t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)

b1 = Button(window, text = "Calculate",  command = BMI)


e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e5.grid(row = 2, column = 0)
t3.grid(row = 2, column = 1)
b1.grid(row = 0, column = 2)

window.mainloop()

