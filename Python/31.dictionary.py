#WAP to print the keys, values & key-Value pair

d = {1:"mango", 2:"Apple", 3:"Grape" }
print("Keys ---")
for k in d.keys():
    print(k)
    
print("Values ---")
for j in d.values():
    print(j)
    
print("Key-Value Pair---")
for k,v in d.items():
    print(k,":",v)    
        
    
# Output
# Keys ---
# 1
# 2
# 3
# Values ---
# mango
# Apple
# Grape
# Key-Value Pair---
# 1 : mango
# 2 : Apple
# 3 : Grape    
    