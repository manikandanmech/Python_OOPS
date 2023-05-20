"""
 Polymorphism====>
    In programming ==> polymorphism means the same function name being used for different types.
"""

# Polymorphism in addition(+) operator
#For integer data types(+)-- arithmetic addition operation:
a=20
b=10
print(a+b)
#for string data types, + operator is used to perform concatenation:
a="maatram"
b="foundation"
print(a+b)


#in_built Polymorphic function
a="abcd"
print(len(a))
b=(10,20,30,40)
print(len(b))


#polymorphism with a function and object===>
class parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot can't swim")
class penguin:
    def fly(self):
        print("penguin can't fly")
    def swim(self):
        print("penguin can swim")

#common interface
def flying_test(bird):
    bird.fly()

#objects
bird1=parrot()
bird2=penguin()

#passing the objects to the common function
flying_test(bird1)
flying_test(bird2)