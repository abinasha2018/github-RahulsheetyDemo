#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__


class Calculator:
    num = 100  #Class variable
    #default constructor
    def __init__(self,a,b):
        self.firstnumber = a #instance variable
        self.secondnumber = b
        print("I am called automatically when object is created... ")

    def getData(self):
        print("I am now executing as method in class")

    def addition(self):

        return self.firstnumber + self.secondnumber + Calculator.num  #Self.num

cal = Calculator(2,3) #Syntax to create objects in python
cal.getData()
print(cal.addition())
print(cal.num)

cal = Calculator(4,5) #Syntax to create objects in python
cal.getData()
print(cal.addition())
print(cal.num)
