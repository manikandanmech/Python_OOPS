"""
Class Attributes in Python
Class attributes belong to the class itself they will be shared by all the instances.
Such attributes are defined in the class body parts usually at the top, for legibility.

1. getattr ( object , name [ , default ] )
object => object whose named attribute's value is to be returned
name => string that contains the attribute's name
default ( Optional ) => The value is returned when the named attribute is not found

2. setattr( object , name , value )
object => object whose named attribute value is to be assigning.
name => The assigned variable name
default => The assigned variable value.

3. delattr( object , name )
object => object whose named attribute value is to be removed.
name => The attribute which is to be removed.

"""


class Student():
    name = "Manikandan"
    age = 20


''' This is Class Attributes '''

# getattr method
print(getattr(Student, 'name'))
print(getattr(Student, 'age'))
print(getattr(Student, 'gender', 'No Such Attribute Found'))

# Dot Notation
print(Student.name)
print(Student.age)

# setattr
setattr(Student, 'name', 'Manikandan')
print(Student.name)

setattr(Student, 'gender', 'Male')
print(Student.gender)

Student.city = "Trichy"
print(Student.city)
print(Student.__dict__)

delattr(Student, "city")
print(Student.__dict__)

del Student.gender
print(Student.__dict__)
