                 #Single Inheritance in Python
"""
 Single Inheritance in Python refers to a situation where a derived class inherits from a single base class.
 The derived class inherits all the attributes and methods of the base class and can also have additional attributes and methods of its own.
 This is the simplest form of inheritance, where a child class inherits from one parent class.
 The child class can access all the public and protected methods and attributes of the parent class.

  Syntax :
         class base1 :
              body of base class
         class derived( base1) :
              body of derived class
"""
class Food:
    company = "Foodie shooter"
    webiste = "www.foodieshooter.com"

    def contact_details(self):
        print("Address :Near Bus Stand ,Pudukkottai")


class shooter_biriyani(Food):
    def __init__(self):
        self.name = "shooter_biriyani"
        self.year = 2023

    def product_details(self):
        print("Name     : ", self.name)
        print("Year     : ", self.year)
        print("Company  : ", self.company)
        print("Website  : ", self.webiste)


shop = shooter_biriyani()
shop.product_details()
shop.contact_details()
