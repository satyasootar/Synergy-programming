#WAP to create a login page using Geometry 

from tkinter import *

# Create the main window
Home = Tk()
Home.geometry("400x400")
Home.title("Login Page")

# Labels and Entries
l1 = Label(Home, text="User Id: ")
l1.place(x=50, y=50)

e1 = Entry(Home)
e1.place(x=150, y=50)

l2 = Label(Home, text="Password: ")
l2.place(x=50, y=100)

e2 = Entry(Home, show="*")
e2.place(x=150, y=100)

# Buttons
b1 = Button(Home, text="Login", bg="green", fg="white")
b1.place(x=50, y=150)

b2 = Button(Home, text="Forgot", bg="orange", fg="white")
b2.place(x=150, y=150)

b3 = Button(Home, text="Cancel", bg="red", fg="white")
b3.place(x=250, y=150)

Home.mainloop()
