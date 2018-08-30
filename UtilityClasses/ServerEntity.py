class Server:

    def __init__(self, capacity, time_randomizer, description=None):
        """
        Server represents a system resource that holds Customers in a container, assigns randomly sampled durations
        to Customers, and possesses a finite capacity.

        :param capacity: Maximum Customers server can contain
        :type capacity: int
        :param time_randomizer: Used to randomly sample duration from different distributions.
        :type class[TimeRandomizer]
        :param description: Text description of Server
        :type description: str
        """

        self.description = description
        self.capacity = capacity
        self.time_randomizer = time_randomizer
        self.server_slots = []

    def add_customer(self, customer):
        """
        Attempts to add Customer to Server. If adding is successful return=True, but if adding Customer will cause
        capacity to be exceeded, return=False.

        :param customer: Customer object to add.
        :type customer: class[Customer]
        :return: bool
        """

        if len(self.server_slots) < self.capacity:
            # add customer with randomized time
            random = self.generate_random()

            customer.server_time_seconds = random
            self.server_slots.append(customer)

            return True
        else:
            return False

    def generate_random(self):
        """
        Uses TimeRandomizer to generate random sample for this Server.

        :return: float
        """
        return self.time_randomizer.generate_random_sample()

    def remove_customer(self, customer):
        """
        Attempts to remove Customer from Server. If Server is empty, return=False.

        :param customer: Customer to remove
        :type customer: class[Customer]
        :return: bool
        """
        if len(self.server_slots) > 0:
            self.server_slots.remove(customer)
            return True
        else:
            return False

    def is_server_full(self):
        """
        Simply checks if Server is full to capacity.

        :return: bool
        """
        if len(self.server_slots) == self.capacity:
            return True
        else:
            return False
