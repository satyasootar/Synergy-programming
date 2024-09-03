# WAP a program to create patterns


n = int(input("Enter the value: "))    


for i in range(1 , n+1 , 1):
    for j in range(0 , i , 1):
        print("*" ,end ="")
    print()    
    
    # output 
    # *
    # **
    # ***
    # ****
       
             
for i in range (1 , n+2 ):
    for j in range( i , n+1 ):
        print(" ", end="")
    for j in range(1 , i  ):
        print("*" ,end="")
    print()    

    # output
    #    *
    #   **
    #  ***
    # ****