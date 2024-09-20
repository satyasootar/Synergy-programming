#WAP to print the number of vowels present in a sentence

d = {}

s = input("Enter the sentence: ").lower()

for i in s:
    if i in 'aeiou': 
        d[i] = d.get(i, 0) + 1 

for k, v in d.items():
    print(f"'{k}' occurs {v} times")
  
# Output
# Enter the sentence: i am satya
# 'i' occurs 1 times
# 'a' occurs 3 times  