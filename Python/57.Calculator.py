#WAP to create a calculator

from tkinter import *

Home = Tk()
Home.title("Addition")
Home.geometry("400x300")  


a, b, c = StringVar(), StringVar(), StringVar()


l1 = Label(Home, text="Number 1: ")
l1.place(x=20, y=30)

e1 = Entry(Home, textvariable=a)
e1.place(x=120, y=30, width=100)

l2 = Label(Home, text="Number 2: ")
l2.place(x=20, y=70)

e2 = Entry(Home, textvariable=b)
e2.place(x=120, y=70, width=100)

l3 = Label(Home, text="Result: ")
l3.place(x=20, y=110)

e3 = Entry(Home, textvariable=c)
e3.place(x=120, y=110, width=100)

# Define the functions for operations
def add():
    try:
        x = int(a.get())
        y = int(b.get())
        z = x + y
        c.set(z)
    except ValueError:
        c.set("Invalid input")

def sub():
    try:
        x = int(a.get())
        y = int(b.get())
        z = x - y
        c.set(z)
    except ValueError:
        c.set("Invalid input")

def mult():
    try:
        x = int(a.get())
        y = int(b.get())
        z = x * y
        c.set(z)
    except ValueError:
        c.set("Invalid input")

def div():
    try:
        x = int(a.get())
        y = int(b.get())
        if y == 0:
            c.set("Cannot divide by zero")
        else:
            z = x / y
            c.set(z)
    except ValueError:
        c.set("Invalid input")


b1 = Button(Home, text="Add", bg="orange", fg="white", command=add)
b1.place(x=20, y=150, width=80)

b2 = Button(Home, text="Sub", bg="orange", fg="white", command=sub)
b2.place(x=110, y=150, width=80)

b3 = Button(Home, text="Mult", bg="orange", fg="white", command=mult)
b3.place(x=200, y=150, width=80)

b4 = Button(Home, text="Div", bg="orange", fg="white", command=div)
b4.place(x=290, y=150, width=80)


Home.mainloop()
