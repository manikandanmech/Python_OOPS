""" Data Abtraction==>
   *Data Abstraction in Python is the process of hiding the real implementation of an application
   from the user and emphasizing only on usage of it.
   *abstract method using @abstractmethod keyword on the top of a method.
   """


from abc import ABC, abstractmethod
class MyClass(ABC):
 @abstractmethod
 def mymethod(self):
  #empty body
  pass




    <i will update here quickly>