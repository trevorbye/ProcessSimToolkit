from UtilityClasses.CustomerEntity import Customer


class InteractionLogic:

    def __init__(self, server_and_queue_wrapper_list, report_entity):
        """
        Accepts a list of wrapper objects and attempts to move Customers through chain of Servers/Queues

        :param server_and_queue_wrapper_list: list of ServerAndQueueWrapper objects
        :type server_and_queue_wrapper_list: list
        :param report_entity: ReportEntity object
        :type report_entity: class[ReportEntity]
        """

        self.server_and_queue_wrapper_list = server_and_queue_wrapper_list
        self.sim_time = None
        self.report_entity = report_entity

    def single_interaction(self, sim_time):
        """
        Processes the interactions between events ONE time.

        :param sim_time:
        :type sim_time: datetime.pyi
        :return: void
        """

        self.sim_time = sim_time

        for wrapper in self.server_and_queue_wrapper_list:

            current_index_position = self.server_and_queue_wrapper_list.index(wrapper)
            last_index_position = len(self.server_and_queue_wrapper_list) - 1

            # first position should be a server (n=1) for processing system arrival distribution
            if current_index_position == 0:
                # look for arrival Server in position 0; throw warning if not server
                arrival_wrapper = self.server_and_queue_wrapper_list[0]

                if not arrival_wrapper.is_server:
                    raise RuntimeWarning("First entity in server/queue wrapper list is not a Server. Must be "
                                         "Server of size n=1 for arrivals.")
                else:
                    arrival_server = arrival_wrapper.server_object

                    # if server is empty, add Customer
                    if len(arrival_server.server_slots) == 0:
                        # do not enter params, add_customer populates duration
                        customer = Customer()
                        arrival_server.add_customer(customer)
                    else:
                        # check if current duration is 0, if so set server entrance time and attempt to move to next
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
                                desc = next_server.description

                                # attempt to add customer to server, if add_customer() returns false, throw warning
                                # because simulation will run infinitely with a zero duration customer and no available
                                # space for it to move to. Always consider using Queues after Servers to avoid this

                                if not next_server.add_customer(cust):
                                    raise RuntimeWarning("No available space in Server" + desc + "for Customer. Consider adding"
                                                         "a Queue after this Server, or expand Server capacity, "
                                                         "otherwise simulation will run infinitely.")
                            else:
                                # add to end of PriorityQueue, no time randomization
                                next_queue = next_position_wrapper.queue_object
                                next_queue.add(cust)

            # process last position, should be Server
            elif current_index_position == last_index_position:

                if not wrapper.is_server:
                    raise RuntimeWarning("Last entity in server/queue wrapper list is not a Server. Must be "
                                         "Server of size n>0 for system exit behavior.")
                else:
                    # find all Customers in last Server with time=0, compute total system time, add to Report object
                    exit_server = wrapper.server_object
                    exit_server_slots = exit_server.server_slots
                    # make copy to remove while iterating
                    list_copy = exit_server_slots

                    if len(exit_server_slots) > 0:
                        for customer in list_copy:
                            if customer.server_time_seconds == 0:
                                # calculate total system time and add to output report
                                total_seconds = (self.sim_time - customer.system_entrance_time).total_seconds()
                                self.report_entity.add_sample(total_seconds)

                                exit_server_slots.remove(customer)

            # if in a middle position, determine whether a server or queue, and attempt to push to next process
            else:
                next_index_position = current_index_position + 1
                next_wrapper = self.server_and_queue_wrapper_list[next_index_position]

                # if Server, see if Customer is finished and attempt to move to next process
                if wrapper.is_server:

                    server_slots = wrapper.server_object.server_slots
                    slots_copy = server_slots

                    if len(server_slots) > 0:
                        for customer in slots_copy:
                            if customer.server_time_seconds == 0:
                                # check next position
                                if next_wrapper.is_server:
                                    next_server = next_wrapper.server_object
                                    desc = next_server.description

                                    if not next_server.add_customer(customer):
                                        raise RuntimeWarning(
                                            "No available space in Server" + desc + "for Customer. Consider adding"
                                            "a Queue after this Server, or expand Server capacity, "
                                            "otherwise simulation will run infinitely.")
                                    else:
                                        server_slots.remove(customer)
                                else:
                                    next_queue = next_wrapper.queue_object
                                    next_queue.add(customer)
                                    server_slots.remove(customer)

                # if queue, simply check next process and attempt to move as many queue items as possible
                else:
                    current_queue = wrapper.queue_object
                    queue_length = len(current_queue.priority_queue)

                    if queue_length > 0:
                        if next_wrapper.is_server:

                            server = next_wrapper.server_object
                            server_full = server.is_server_full()

                            while not server_full and queue_length > 0:
                                cust = current_queue.remove()
                                queue_length = len(current_queue.priority_queue)

                                server.add_customer(cust)
                                server_full = server.is_server_full()

                        else:
                            raise RuntimeWarning("Two Queues are linked back-to-back. Consider adding a Server"
                                                 " in between Queues to avoid redundancy and improve run time.")

    def process_interactions(self, sim_time):
        """
        Runs interaction logic twice to ensure all movement possibilities are performed at each time step.

        :param sim_time: datetime.pyi
        :return: void
        """
        self.single_interaction(sim_time)
        self.single_interaction(sim_time)
