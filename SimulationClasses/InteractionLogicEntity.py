from UtilityClasses.CustomerEntity import Customer


class InteractionLogic:

    # accepts a list of wrapper objects and attempts to move Customers through chain of Servers/Queues
    def __init__(self, server_and_queue_wrapper_list, sim_time):
        self.server_and_queue_wrapper_list = server_and_queue_wrapper_list
        self.sim_time = sim_time

    def process_interactions(self):

        for wrapper in self.server_and_queue_wrapper_list:

            current_index_position = self.server_and_queue_wrapper_list.index(wrapper)
            last_index_position = len(self.server_and_queue_wrapper_list) - 1

            if current_index_position == 0:
                # look for arrival Server in position 0; throw warning if not server
                arrival_wrapper = self.server_and_queue_wrapper_list[0]

                if not arrival_wrapper.is_server:
                    raise RuntimeWarning("First entity in server/queue wrapper list is not a Server. Must be "
                                         "Server of size n=1 for arrivals")
                else:
                    arrival_server = arrival_wrapper.server_object

                    # if server is empty, add Customer
                    if len(arrival_server.server_slots) == 0:
                        # do not enter params, add_customer populates duration
                        customer = Customer()
                        arrival_server.add_customer(customer)
                    else:
                        # check if current duration is 0, if so set property entrance time and attempt to move to next
                        current_arrival_customer = arrival_server.server_slots[0]

                        if current_arrival_customer.server_time_seconds == 0:
                            # remove from arrival server and set system entrance time
                            cust = arrival_server.server_slots.pop(0)
                            cust.system_entrance_time = self.sim_time

                            # attempt to add to next Server/Queue
                            next_index_position = current_index_position + 1
                            next_position_wrapper = self.server_and_queue_wrapper_list[next_index_position]

                            if next_position_wrapper.is_server:
                                next_server = next_position_wrapper.server_object
                            else:
                                next_queue = next_position_wrapper.queue_object






