#WAP to filter all the prime number from the given list

def Prime(n):
    if n<2:
        return False
    
    for i in range (2, n//2+1):
        if(n % i == 0):
            return False
    return True    

def Comp(n):
    if n<2:
        return True
    
    for i in range (2, n//2+1):
        if(n % i == 0):
            return True
    return False   

A = [1,2,3,4,5,6,7,8,9,0,23,34,12,53,65]

Cl = list(filter(Comp, A))
Pl = list(filter(Prime, A))
print("Prime no:",Pl)
print("Composite no:",Cl)


# Output
# Prime no: [2, 3, 5, 7, 23, 53]
# Composite no: [1, 4, 6, 8, 9, 0, 34, 12, 65]
