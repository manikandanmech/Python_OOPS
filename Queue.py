"""
Queue===>
     Queue follows the First In First Out (FIFO) rule
the item that goes in first is the item that comes out first.

Allows the following operations:
  Enqueue: Add an element to the end of the queue
  Dequeue: Remove an element from the front of the queue
  IsEmpty: Check if the queue is empty
  IsFull: Check if the queue is full
  Peek: Get the value of the front of the queue without removing it


Queue in Python can be implemented in the following ways:
 1.list
 2.collections.deque
 3.queue.Queue

"""
# 1) List
# implementing Queue using List :
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print(queue)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("After pop operation:",queue)

#2.collections.deque

from collections import deque
queue=deque()
queue.append(10)
queue.append(100)
queue.append(1000)
queue.append(10000)
print(queue)
print(queue.popleft())
print(queue.popleft())
print("After removing:",queue)