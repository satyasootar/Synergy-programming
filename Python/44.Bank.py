import random

class Account:
    name = ""
    acNO = 0
    balance = 0
    def __init__(self, nm, ac, ba):
        self.name = nm
        self.acNo = ac
        self.balance = ba
        
    def deposit(self):
        n = int(input("Enter the amount you want to deposit: "))
        self.balance += n
        print(f"{n} deposited. New balance: {self.balance}")
        
    def withdraw(self):
        n = int(input("Enter the amount you want to withdraw: "))
        if n <= self.balance:
            self.balance -= n
            print(f"{n} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance.")
        
    def display(self):
        print("Name =", self.name,
              "\nAccount no =", self.acNo,
              "\nBalance =", self.balance)

def generate_account_number():
    return random.randint(1000000000, 9999999999)


Name = input("Enter your name: ")
acNO = generate_account_number()  # Generate a random account number
balance = int(input("Deposit the starting balance: "))      
obj = Account(Name, acNO, balance) 

while True:
    print("\n1. Deposit")               
    print("2. Withdraw")
    print("3. Display")
    print("4. Exit")
    
    n = int(input("Enter your choice: "))
    
    if n == 1:
        obj.deposit()
        
    elif n == 2:
        obj.withdraw()
        
    elif n == 3:
        obj.display() 
        
    elif n == 4:
        print("Exiting the Bank.")
        break
        
    else:
        print("Invalid choice")     


# #output
# Enter your name: satya
# Deposit the starting balance: 100

# 1. Deposit
# 2. Withdraw
# 3. Display
# 4. Exit
# Enter your choice: 1
# Enter the amount you want to deposit: 100
# 100 deposited. New balance: 200

# 1. Deposit
# 2. Withdraw
# 3. Display
# 4. Exit
# Enter your choice: 2
# Enter the amount you want to withdraw: 22
# 22 withdrawn. New balance: 178

# 1. Deposit
# 2. Withdraw
# 3. Display
# 4. Exit
# Enter your choice: 3
# Name = satya 
# Account no = 8132695571 
# Balance = 178

# 1. Deposit
# 2. Withdraw
# 3. Display
# 4. Exit
# Enter your choice: 4
# Exiting the Bank.