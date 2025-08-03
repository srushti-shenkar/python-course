valid=False
while not   valid:#using nested loop 
    try:
        n=int(input("enter a number:"))
        #enter a even number number
        while n%2==0:
            print("bye")
        valid=True
    except ValueError:
        print("Invalid")

