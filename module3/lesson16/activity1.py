#class creation 
class myClass:
    #private variable
    __privateVar=27
    #pricate method
    def __privMeth(self):
        print("I am inside myClass")

    #function to print value of private variable
    def hello(self):
        print("Private Variable value:",myClass.__privateVar)
#object creation and method call
foo=myClass()
foo.hello()
foo.__privMeth