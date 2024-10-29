#WAP to copy the contents of an existing file into another file in python

P = open("myFile.txt", "r")
value = P.read()
P.close

P = open("paste.txt", "w")
P.write(value)
P.close

P = open("paste.txt", "r")
print(P.read())
P.close()

# Output
# Hello
# Hello 2
