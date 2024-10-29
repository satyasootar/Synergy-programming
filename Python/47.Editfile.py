#WAP to create a file name "myFile.txt" to write a message into it. Then read the message in it.

P = open("myFile.txt","w")
P.write("Hello\n")
P.write("Hello 2\n")
P.close()

P = open("myFile.txt","r")
print(P.read())
P.close()


# Output
# Hello
# Hello 2
