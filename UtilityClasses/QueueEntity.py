from collections import deque


# slightly modifying methods in deque class for an unambiguous queue implementation
class PriorityQueue:

    def __init__(self, description=None):
        self.priority_queue = deque([])
        self.description = description

    # adds to last in line
    def add(self, customer):
        return self.priority_queue.append(customer)

    # returns first object in queue without removing it
    def peek(self):
        return self.priority_queue[0]

    # removes and returns first in line
    def remove(self):
        return self.priority_queue.popleft()