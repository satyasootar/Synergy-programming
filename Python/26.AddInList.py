#WAP to declare a list and add elements into in dynamically and display then in a sorted manner.

k=[]
n=int(input("Enter the length: "))
for i in range(n):
    p = int(input("Enter the value: "))
    k.append(p)
k.sort()
print(k)    

# output
# Enter the length: 5
# Enter the value: 21
# Enter the value: 12
# Enter the value: 34
# Enter the value: 56
# Enter the value: 3 
# [3, 12, 21, 34, 56]