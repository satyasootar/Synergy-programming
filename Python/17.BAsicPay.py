basicPay = int(input("Enter the basic pay \n"))
if(basicPay >= 5000):
    Da = basicPay*0.7
    Ta = basicPay*0.5
    HRA = basicPay*0.1
elif(basicPay >= 3000):
    Da = basicPay*0.7
    Ta = basicPay*0.3
    HRA = basicPay*0.05
else:
    Da = basicPay*0.7
    Ta = basicPay*0.15
    HRA = basicPay*0.1  
    
salary = basicPay + Ta + Da + HRA

print("Total salary =" , salary)            