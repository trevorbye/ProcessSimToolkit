import random


class Customer:

    def __init__(self):
        self.system_entrance_time = 0
        self.server_time_seconds = 0

        # create random unique customer id
        self.customer_id = random.randint(1, 10000000)

    def get_server_time(self):
        return self.server_time_seconds

    def set_server_time(self, time_seconds):
        self.server_time_seconds = time_seconds


