# WAP to find the year is leap year or not

x= int(input("Enter a year \n"))
if(x%4 == 0):
    if(x%100 == 0):
        if(x%400 == 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap year")
else:
    print("Not a leap year")                    
    