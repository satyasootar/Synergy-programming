#WAP to input a sentence & count each letter in it using dictionary

d ={}
s= input("Enter the sentence: ")
for i in s:
    d[i] = d.get(i ,0)+1
for k,v in d.items():
    print(k,"Occur", v ,"times")    
    
    # Output
    # Enter the sentence: wwqredccc
    # w Occur 2 times
    # q Occur 1 times
    # r Occur 1 times
    # e Occur 1 times
    # d Occur 1 times
    # c Occur 3 times