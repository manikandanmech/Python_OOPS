                                                       #Property Decorator in Python
"""
Python @property is one of the built-in decorators
@property decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property().
"""

class student :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #>> self.msg = self.name + " is " + str(self.age) + " years old"

    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " years old"


o = student("Kanmani",18)
print(o.name)
print(o.age)
print(o.msg)
o.age = 45
print(o.msg)