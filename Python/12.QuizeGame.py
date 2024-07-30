print("WELCOME TO THE GAME")
score = 0

ans = input("Ready to start 😏 y/n")
if ans == "y":
    ans = input("1. Who discover Python language? \n a.Guido   b.Bill   C.John   d.Satya ")

    if ans == "a":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")
        
    
    ans = input("2. What is the fundamental building block of HTML? \n  a.Form  b.div  c.Tag   d.link ")
    if ans == "c":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")     
        
    ans = input("3. What provides additional information about HTML elements? \n  a.Select   b.Attributes   c.class   d.script")
    if ans == "b":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")
                 
   
    ans = input("4. Which HTML element is used for collecting user input? \n  a.Input   b.Form   c.pokemon   d.Something")
    if ans == "b":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")
        
        
    ans = input("5. What technology is used to style HTML elements? \n   a.CSS    b.Script   c.React   d.Tailwind")
    if ans == "a":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")
        
    
    ans = input("6. What HTML element is used to create clickable links? \n  a.Anchor   b.HperLink   c.meta   d.data")
    if ans == "b":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")
        
        
        
    ans = input("7. What is used to store data in a Java program? \n   a.Local storage   b.Variable  c.constant  d.data Storage")
    if ans == "b":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")
        
        
        
    ans = input("8. What Java construct is used to repeatedly execute a block of code? \n    a.swap    b.queue   c.Loop   d.Pix")
    if ans == "c":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")
        
        
        
    ans = input("9. What is used in Python to define blocks of code? \n   a.Curly Bracket   b.Square Bracket   c.Semi colon   d.Indentation")
    if ans == "d":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")
        
        
    ans = input("10 . What feature of Java allows one class to inherit the properties and methods of another class? \n   a.Polymorphism   b.Encapsulation   c.Data abstraction  d.Inheritance   ")
    if ans == "d":
        score+=1
        print("Oh my God, You are a Genius😇 \n")
    else:
        print("Ah. you are wrong😫 \n")       
    
    
    if score<3 :
        print("Your Score is =", score, "You are so bad that even a child is more inteligent then you")
    elif score < 6 :
        print("Your Score is =", score,"Try to study a little bit😶‍🌫️")  
    elif score == 0 :
        print("Your Score is =", score,"Go and die 💀")         
    else :
        print("Your Score is =", score, "Congratulations🥳, You are among the 99.9% genius")   
  
    print("Thank you visit again🙏")
else:
    print("Ha HA Loser 😒🤬🤮")                                                            