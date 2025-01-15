# Q1. Write a program to implement a Queue using two stacks.
"""
Here's how we can implement a Queue using two stacks.
The idea is to use one stack for enqueue operations and another stack for dequeue operations.
When dequeueing, if the second stack is empty, transfer all the elements from the first stack to the second.
Which reverse the order, and then pop from the second stack.

"""

class QueueUsingStacks:
	def __init__(self):
		# two stack 
		self.stack1 = []
		self.stack2 = []
		
	# Enqueue an element into the queue 
	def enqueue(self, element):
		self.stack1.append(element)
		
	# Dequeue an element from the queue 
	def dequeue(self):
		if not self.stack1 and not self.stack2:
			return "Queue is empty"
			
		if not self.stack2:
			# transfer elements from stack1 to stack2 
			while self.stack1:
				self.stack2.append(self.stack1.pop())
				
		return self.stack2.pop()
		
	# check if the queue is empty 
	def is_empty(self):
		return not self.stack1 and not self.stack2 
		
	# Peek the front element of the queue 
	def front(self):
		if not self.stack1 and not self.stack2: 
			return "Queue is empty"
		
		if not self.stack2:
			# transfet elements from stack1 to stack2 
			while stack1:
				self.stack2.append(self.stack1.pop())
				
		return self.stack2[-1]
		
		
	
# Example 

queue = QueueUsingStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.front())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.is_empty())
