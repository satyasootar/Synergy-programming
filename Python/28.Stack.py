#WAP to create a stack of a given size and perform push() & pop() operation using methods and list

def push(stack):
    x = int(input("Enter the number you want to add: "))
    return stack.append(x)
    
def pop(stack):
    print(f"deleted: {stack.pop()}")   

def display(stack):
    print(f"You stack is {stack}")
    
stack = []
size = 5
   
while(1):
    print("1. Push item \n2. Pop item \n3. Exit\n")
    n = int(input("Enter your choice: ")) 
    
    if(n == 1):
        if(len(stack) <= size):
           push(stack)
           display(stack)
        else:
            print("Overflow") 
    
    elif(n== 2):
      pop(stack)
      display(stack)  
      
    elif(n == 3):
        display(stack) 
        exit()  
         
    
    else:
        print("Ivalid option , choose again")   
      
       
      
      