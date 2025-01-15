# Using deque (maxlen=N) creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is automatically removed .

from collections import deque 
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)

print (f"Q: {q}")

q.append(4)
print(f"Q: {q}")

q.append(5)
print(f"Q: {q}")


# A deque can be used whenever we need a simple queue structure. If we don't give it a maximum size, we get an unbound queue that lets us append and pop items in either and.

q = deque()
q.append(1)
q.append(2)
q.append(3)

print(f"Q: {q}")

q.appendleft(4)

print(f"Q: {q}")

q.pop()
print(f"Q: {q}")

q.popleft()
print(f"Q: {q}")

# Note: Adding or popping items from either and of a queue has O(1) complexity. This is unlike  a list where inserting or removing items from the front of the list is O(N).
