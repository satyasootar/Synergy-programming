# WAP to implement Queue functions 

def enqueue(queue):
    if len(queue) < size:
        x = int(input("Enter the number you want to add: "))
        queue.append(x)
    else:
        print("Overflow")

def dequeue(queue):
    if len(queue) > 0:
        print(f"Removed: {queue.pop(0)}")
    else:
        print("Underflow")

def display(queue):
    print(f"Your queue is: {queue}")

queue = []
size = 5

while True:
    print("1. Enqueue item \n2. Dequeue item \n3. Exit\n")
    n = int(input("Enter your choice: "))
    
    if n == 1:
        enqueue(queue)
        display(queue)
    
    elif n == 2:
        dequeue(queue)
        display(queue)
    
    elif n == 3:
        display(queue)
        break
    
    else:
        print("Invalid option, choose again")
 