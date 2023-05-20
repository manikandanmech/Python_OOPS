"""
Stack====>
          A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
          It means the last element inserted inside the stack is removed first


**Push ==> is used for inserting an element in a stack
**Pop  ==>  is used to removal an element in a stack.

>>Functions associated with Stack
  push(x)-it is used to insert the element at the end of a stack
  pop()-It is used to remove the topmost/last element of a stack
  size()-gives the size/length of a stack
  top()-give reference of last element present in stack
  empty()-returns true for an empty stack

"""
#Implementation of Stack
   #Several ways to implement stack in python:
   #1) List
"""""
#==>Implementation using List
    List in python can be used as stack
    append()- It is used to insert the element
    pop()-It is used to remove the last element  """
#Logic
stack=[]
stack.append("mani")
print(stack.pop())

#implementation using List
stack=[]
stack.append("welcome")
stack.append("to")
stack.append("Maatram Foundation 😍")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


#2) collections.deque
"""
====> Implementation using collection.deque
    Stacks in python are created by the collection module which provides deque class.
    append and pop operations are faster in deque as compare to list. """
#Logic :
from collections import deque
stack = deque()
stack.append("mani")
print(stack.pop())

#implementation using deque
from collections import deque
stack=deque()
stack.append("welcome")
print(stack)
stack.append("to")
stack.append("Mr Cooper")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


# 3) queue.LifoQueue
"""""
====>Functions available in queue module
     get() - It is used to remove the element from the queue.
     maxsize() - used to put the maximum number of items allowed in queue.
     empty() - It returns true, when queue is empty else false.
     full()-When queue is full returns True.
     put(x) - It is used to insert x in queue.
     qsize() - gives the size of a queue  
"""""
#implementation using queue:
from  queue import LifoQueue
stack=LifoQueue(maxsize=3)
stack.put(1)
stack.put(2)
stack.put(3)
print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())

