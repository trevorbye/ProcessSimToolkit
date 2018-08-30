from collections import deque


class PriorityQueue:

    def __init__(self, description=None):
        """
        Slightly modifying methods in deque class for an unambiguous queue implementation.

        :param description: Text description of Queue.
        :type description: str
        """
        self.priority_queue = deque([])
        self.description = description

    def add(self, customer):
        """
        Adds Customer to last position in line.

        :param customer: Customer object to add.
        :type customer: class[Customer]
        :return: class[Customer]
        """
        return self.priority_queue.append(customer)

    def peek(self):
        """
        Returns first object in queue without removing it.

        :return: class[Customer]
        """
        return self.priority_queue[0]

    def remove(self):
        """
        Removes and returns first in line.

        :return: class[Customer]
        """
        return self.priority_queue.popleft()