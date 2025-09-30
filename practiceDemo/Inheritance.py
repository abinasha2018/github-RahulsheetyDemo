class Parent():
    def greet(self):
        return "Hello from Parent"


class Child(Parent):

    def __init__(self,title):
        self.title=title


    def greet(self):
        return super().greet() + " and Hello from Child " +self.title


c=Child("Abinasha")
print(c.greet())