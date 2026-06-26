# Implementing a Queue in Python
#Method 1: Using list
queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Initial queue:", queue)

# Dequeue
print("Dequeued:", queue.pop(0))
print("Queue after dequeue:", queue)


#Method 2: Using collections.deque
from collections import deque

queue = deque()

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Initial queue:", queue)

# Dequeue
print("Dequeued:", queue.popleft())
print("Queue after dequeue:", queue)

