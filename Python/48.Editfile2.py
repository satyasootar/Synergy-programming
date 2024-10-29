#WAP to show the use of seek and tell.

P = open("myFile2.txt","w")
P.write("My name is satya, ")
P.write("I am a developer\n")
P.close()

P = open("myFile2.txt","r")
print(P.read())

P.seek(3)
print("The Pointer moves to the 4th position and prints: ",P.read())

print("The pointer is at: " , P.tell())

P.close()

# OUTPUT
# My name is satya, I am a developer

# The Pointer moves to the 4th position and prints:  name is satya, I am a developer

# The pointer is at:  35