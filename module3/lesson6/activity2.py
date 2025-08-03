try:
    num1,num2=eval(input("enter two numbers,separated by a comma:"))
    result=num1/num2
    print("result is",result)
#using multiple except block for different type of error

except ZeroDivisionError:
    print("division by zero is a error")
except SyntaxError:    
    print("comma is missing.Enter numbers separated by comma ike this 1,2")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what")
