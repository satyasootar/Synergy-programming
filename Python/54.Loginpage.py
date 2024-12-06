#WAP to create a login page

from tkinter import *
Home = Tk()
Home.title("Login Page")

l1 = Label(Home, text = "User Id: ").grid(row= 0, column = 0)
e1= Entry(Home).grid(row = 0, column = 1)

l2 = Label(Home, text = "Password: ").grid(row= 1, column = 0)
e2= Entry(Home).grid(row = 1, column = 1)

b1= Button(Home, text= "Login", bg="Green", fg="white").grid(row= 2, column = 0)
b2= Button(Home, text= "Forgot", bg="Orange", fg="white").grid(row= 2, column = 1)
b3= Button(Home, text= "Cancel", bg="red", fg="white").grid(row= 2, column = 2)


Home.mainloop()