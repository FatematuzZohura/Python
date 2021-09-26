from tkinter import *

window = Tk()

window.title("Converter app")



def hour():


    Second = int(e2_value.get()) * 3600

    t1.delete("1.0", END)
    t1.insert(END, Second)


e1 = Label(window, text="Enter the time in Hour")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text='Second')
t1 = Text(window, height=1, width=20)
b1 = Button(window, text="Convert", command=hour)
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
t1.grid(row=2, column=0)
b1.grid(row=0, column=2)
window.mainloop()