                                              #Static Method in Python

"""
A static method in Python is a method that belongs to a class rather than an instance of the class. 
It can be called on the class itself, rather than on an instance of the class.
Static methods are defined using the @staticmethod decorator, and do not have access to any class-specific state.
They are typically used for utility functions that don't need to access any instance-specific data.
"""

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name : ", self.name, "  Age : ", self.age)

    @staticmethod
    def welcome():
        print("Welcome to our Institution")


s1 = student("Mani", 20)
s1.printDetail()
s1.welcome()


s2 = student("Raja", 45)
s2.printDetail()
s2.welcome()