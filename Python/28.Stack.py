#WAP to create a stack of a given size and perform push() & pop() operation using methods and list

def push(stack, size):
    if len(stack) < size:
        x = int(input("Enter the number you want to add: "))
        stack.append(x)
    else:
        print("Overflow: The stack is full.")

def pop(stack):
    if len(stack) > 0:
        print(f"Deleted: {stack.pop()}")
    else:
        print("Underflow: The stack is empty.")

def display(stack):
    print(f"Your stack is: {stack}")

stack = []
size = 5

while True:
    print("1. Push item \n2. Pop item \n3. Exit\n")
    n = int(input("Enter your choice: "))
    
    if n == 1:
        push(stack, size)
        display(stack)
    
    elif n == 2:
        pop(stack)
        display(stack)
    
    elif n == 3:
        display(stack)
        break
    
    else:
        print("Invalid option, choose again")

       
      
      