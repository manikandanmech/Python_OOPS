         #Property Decorator Getter Setter in Python
"""
In Python, property decorators are used to define getter, setter, and deleter methods for class properties.
They allow for the encapsulation of data, by controlling access to the underlying data.
 Property decorators are applied to methods and define how a property value can be retrieved, set, or deleted.

Getter: A getter is a method that is used to retrieve the value of a property. 
The getter method is decorated with the @property decorator and has no arguments.


Setter: A setter is a method that is used to set the value of a property.
The setter method is decorated with the @<property_name>.
setter decorator and takes one argument, the new value for the property.
"""

class student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 6.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, t):
        if t < 0 or t > 600:
            print("Invalid Total and can't Change")
        else:
            self._total = t

o = student(550)
print("Total   : ", o.total)
print("Average : ", o.average())
o.total = 650
print("Total   : ", o.total)
print("Average : ", o.average())