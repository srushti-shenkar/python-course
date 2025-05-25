print("select your ride:")
print("1.bike")
print("2.car")

#take input of number 1 or 2
#select your ride
choice=int(input("enter your choice:"))
#user entering option 1
if(choice==1): #condition 1 outer if statement
    print("1,scooty\n")
    print("2.scooter\n")

  #condition for selecting the type of bike
    choice2=int(input("enter your choice2:"))
    if choice2==1:#inner if statement
        print("you have selected scooty")
    else:
        print("you have slected scooter")   

 #user entering option 2
elif(choice==2):#outer elif statement
    print("what type of jeep")
    print("1.sedan")
    print("2.XUV")
    choice3=int(input("enter your choice3:"))

    if choice3==1: #inner if statement
 #condition for selecting the type of car    
        print("you have selected sedan")
    else:
        print("you have selected a XUV")

else: #outer else statement             
    print("wrong choice")








   
    


