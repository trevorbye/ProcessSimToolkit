

class Server:

    def __init__(self, capacity, time_randomizer, description=None):
        self.description = description
        self.capacity = capacity

        # time_randomizer is an object of type TimeRandomizer
        self.time_randomizer = time_randomizer
        self.server_slots = []

    def add_customer(self, customer):
        if len(self.server_slots) < self.capacity:
            # add customer with randomized time
            random = self.generate_random()

            customer.server_time_seconds = random
            self.server_slots.append(customer)

            return True
        else:
            return False

    def generate_random(self):
        return self.time_randomizer.generate_random_sample()

    def remove_customer(self, customer):
        if len(self.server_slots) > 0:
            self.server_slots.remove(customer)
            return True
        else:
            return False

    def is_server_full(self):
        if len(self.server_slots) == self.capacity:
            return True
        else:
            return False

