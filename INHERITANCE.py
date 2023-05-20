"""
INHERITANCE===>
*The method of inheriting the properties of parent class into a child class is known as inheritance.
*It is an OOP concept."""
class Parent():
    def first(self):
        print('function 1')
class Child(Parent):
    def second(self):
        print('function 2')
obj= Child()
obj.first()
obj.second()
#<access the parent class function using the child class object>

#Types Of Inheritance

# 1)Single Inheritance:
"""When a child class inherits only a single parent class"""
class father():
    f_name="chinnathambi"
    f_age=70
class son(father):
    s_name="vasu"
    s_age=22
obj=son()
print(obj.f_name)
print(obj.s_name)

# 2)Multiple Inheritance
"""When a child class inherits from more than one parent class"""
#base class
class father():
    f_name="chinnathambi"
    f_age=70
#base class
class mother():
    m_name="santhi"
    m_age=45
#child class
class son(father,mother):
    s_name="mani"
    s_age=22
obj=son()
print(obj.m_name)
print(obj.f_name)
print(obj.s_name)


# 3)Multilevel Inheritance
"""When a child class becomes a parent class for another child class"""
#base class
class g_father():
    g_name="gopal"
    g_age=79
#child class
class father(g_father):
    f_name="chinnathambi"
    f_age=70
class son(father):
    s_name="mani"
    s_age=22
obj=son()
print(obj.g_name)
print(obj.f_name)
print(obj.s_name)

# 4)Hierarchical Inheritance
"""Hierarchical inheritance involves multiple inheritance from the same base or parent class"""
#base class
class father():
    f_name="chinnathambi"
    f_age=70
#child class
class daughter(father):
    d_name="vasuki"
    d_age=45
#child class
class son(father):
    s_name="mani"
    s_age=22
obj=son()
obj2=daughter()
print(obj.s_name)
print(obj2.d_name)





