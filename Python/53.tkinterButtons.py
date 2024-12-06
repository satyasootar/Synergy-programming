#WAP to create a color buttons on TK.

from tkinter import *
Home = Tk()

b1= Button(Home, text= "RED", bg="red", fg="white")
b2= Button(Home, text= "BLUE", bg="blue", fg="white")
b3= Button(Home, text= "YELLOW", bg="yellow", fg="black")
b4= Button(Home, text= "GREEN", bg="green", fg="white")

b1.pack()
b2.pack()
b3.pack()
b4.pack()


Home.mainloop()