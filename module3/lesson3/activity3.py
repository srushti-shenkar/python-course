def add(P,Q):
    #this function is used for adding two numbers
    return P+Q
def subtract(P,Q):
    #this function is used for subtracting two numbers
    return P-Q
def multiply(P,Q):
    #this funtion is used for multiplying two numbers
    return P*Q
def divide(P,Q):
    #this fuction is used to divide two numbers
    return P/Q
 
 # now we wll take inputs from the user
print("please select the operations")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

choice=input("please enter choice(a/b/c/d):")
num_1=int(input("please enter the first number:"))
num_2=int(input("please enter the second number"))

if choice=='a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))

elif choice=='a':
    print (num_1,"-",num_2,"=",subtract(num_1,num_2))

elif choice=='c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))

elif choice=='d':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
 
else:
    print("this is an invalid input")

