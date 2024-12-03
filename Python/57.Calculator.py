#WAP to crate a addition interface

from tkinter import *

Home = Tk()
Home.title("Addition")

a = StringVar()
b= StringVar()
c = StringVar()

l1 = Label(Home, text = "Number 1: ").grid(row= 0, column = 0)
e1= Entry(Home, textvariable = a).grid(row = 0, column = 1)

l2 = Label(Home, text = "Number 2: ").grid(row= 1, column = 0)
e2= Entry(Home, textvariable = b).grid(row = 1, column = 1)

l2 = Label(Home, text = "Result: ").grid(row= 2, column = 0)
e2= Entry(Home, textvariable = c).grid(row = 2, column = 1)

def add():
    x = int(a.get())
    y = int(b.get())
    
    z = x + y
    c.set(z)
    
def sub():
    x = int(a.get())
    y = int(b.get())
    
    z = x - y
    c.set(z)    

def mult():
    x = int(a.get())
    y = int(b.get())
    
    z = x * y
    c.set(z)
    
def div():
    x = int(a.get())
    y = int(b.get())
    if y == 0:
        c.set("Cannot divide by zero")
    else:
        z = x / y
        c.set(z) 


b1= Button(Home, text= "Add", bg="Orange", fg="white" , command=add).grid(row= 3, column = 0)
b2= Button(Home, text= "Sub", bg="Orange", fg="white" , command=sub).grid(row= 3, column = 1)
b3= Button(Home, text= "Mult", bg="Orange", fg="white" , command=mult).grid(row= 3, column = 2)
b4= Button(Home, text= "Div", bg="Orange", fg="white" , command=div).grid(row= 3, column = 3)


Home.mainloop()
