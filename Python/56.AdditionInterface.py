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

b1= Button(Home, text= "Add", bg="Green", fg="white" , command=add).grid(row= 3, column = 2)


Home.mainloop()
