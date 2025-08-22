import random #importing module
playing=True#initialise
number=str(random.randint(10,20))#random in-built
print("i will generate a number from 10 to 20  and you have to guess one digit at a time.")
print("the game ends when you get one hero!")
#iterate loop till the condition is true  
while playing:
    guess=input("give me your best guess!\n")
    if number==guess:
        print("you win the game")
        print(",numberthe number was")
        break
    else:
        print("your guess isnt quite right, try again.\n")
 
    
