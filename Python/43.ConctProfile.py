#WAP to access your profile and display them

class Profile:
    name = ""
    roll = ""
    age = 0
    
    def __init__(self, nm, roll, age):
        self.name = nm
        self.roll = roll
        self.age = age
       
    def display(self):
        print("Your Name = ", self.name,"\nYour Roll = ", self.roll, "\nYour age = ", self.age)
        
        
obj = Profile("Satya", "CS-23-51", 19)
obj.display()        

# output 
# Your Name =  Satya 
# Your Roll =  CS-23-51 
# Your age =  19