import random


class Customer:

    def __init__(self, current_sim_time=None, server_time_seconds=None):
        self.system_entrance_time = current_sim_time
        self.server_time_seconds = server_time_seconds

        # create random unique customer id
        self.customer_id = random.randint(1, 10000000)


