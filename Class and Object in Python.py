                                           #Class and Object in Python
"""
Python is an object oriented programming language. Almost everything in Python is an object is simply a collection of data (variables) and methods (functions) that act on those data. A Class is like an object constructor, or a "blueprint" for creating objects. 
Example :
   A dog has states - color, name, breed as well as behaviors – wagging the tail, barking, eating. An object is an instance of a class.

Syntax of Class:
      class Class_Name :
            # statements

Example of Class:
      class student :
            name = " Tutor joe's "
            age = 30
Syntax of Object:
      object_name = class_name ( arguments )
Example of Object:
      s = student ( )
  """


class food():
    pass
a = 200
print(type(a))
print(type(food))
veg=food()
print(isinstance(veg,food))
print(isinstance(a,int))
print(type(veg))
