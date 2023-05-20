"""
CONSTRUCTOR===>
  *A constructor is a unique function that gets called automatically when an object is created of a class.
 *The main purpose of a constructor is to initialize or assign values to the data members of that class.
 """
#Syntax of Python Constructor

def __init__(self):
    #initializations

  """""
   init is one of the reserved functions in Python.
In Object Oriented Programming, it is known as a constructor.
The word init, which is prefixed and suffixed with double underscores with a pair of brackets,==> __init__().
  """
#Types of Constructors in Python.
 # 1.Parameterized Constructor
"""
     A constructor with defined parameters or arguments is called a parameterized constructor.
     This takes one or more arguments
"""""
class Employee:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    # display object
    def show(self):
        print(self.name, self.age, self.salary)
# creating object of the Employee class
mani = Employee('mani', 20, 10000)
mani.show()
raj = Employee('raj', 21, 85000)
raj.show()


# 2.Non-Parameterized Constructor:
class Company:
    # no-argument constructor
    def __init__(self):
        self.name = "Manikandan"
        self.address = "pudukkottai"
    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)
# creating object of the class
cmp = Company()
# calling the instance method using the object
cmp.show()

""""""
# 3.Default Constructor:
"""It does not perform any task but initializes the objects. It is an empty constructor without a body."""
class Employee:
    def display(self):
        print('Hello Akka')
emp = Employee()
emp.display()








