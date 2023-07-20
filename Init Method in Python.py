
                   #Init Method in Python
"""
The __init__ method, also known as the constructor method, is a special method in Python classes that gets called automatically when a new instance of the class is created.
The __init__ method is used to initialize the attributes of the class and set them to the default values.
"""


class user:
    def __init__(self, name):
        print("Call When new Instance Created")
        self.name = name
    def printall(self):
        print("Name : ", self.name)


o1 = user("Manikandan")

o1.printall()
print(o1.__dict__)
o2 = user("Mani")
o2.printall()
print(o2.__dict__)
print(user.__dict__)