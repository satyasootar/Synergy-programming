#WAP to create a dictionary containing RollNO, as KEY and Percentage as MARK. Filter the rollNo of those student greater than 70%, 80% and  90% mark
data = {
    1: 10,
    2: 20,
    3: 50,
    4: 72,
    5: 83,
    6: 96,
    7: 86
}
print("Roll | Percentage")
for k , v in data.items():

    print(k ,"   :  ", v)
    
    
    
def Agrade(n):
        if(data[n]>= 90):
            return True
        
def Bgrade(n):
        if(data[n]>= 80):
            return True        
        
def Cgrade(n):
        if(data[n]>= 70):
            return True        
                
A = list(filter(Agrade, data))
B = list(filter(Bgrade, data))
C = list(filter(Cgrade, data))


    
    
print("More then 90%: ",A)
print("More then 80%: ",B)
print("More then 70%: ",C)


# Output
# Roll | Percentage
# 1    :   10
# 2    :   20
# 3    :   50
# 4    :   72
# 5    :   83
# 6    :   96
# 7    :   86
# More then 90%:  [6]
# More then 80%:  [5, 6, 7]
# More then 70%:  [4, 5, 6, 7]