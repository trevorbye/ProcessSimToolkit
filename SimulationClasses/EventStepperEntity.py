class EventStepper:

    def __init__(self):
        pass

    # function accepts a list of ServerAndQueueWrapper objects
    @staticmethod
    def evaluate_time_steps(server_and_queue_wrapper_list):

        # first build all time vals
        time_val_list = []

        for wrapper_object in server_and_queue_wrapper_list:

            # only get time vals from Server objects, Customers in PriorityQueues simply advance when available
            if wrapper_object.is_server:
                server_object = wrapper_object.server_object
                server_slot_list = server_object.server_slots

                if len(server_slot_list) > 0:
                    for customer in server_slot_list:
                        time_val = customer.server_time_seconds
                        time_val_list.append(time_val)

        # minimum val becomes the step value. Decrease all Server Customer time vals by min_time_val, and step
        # simulation forward by min_time_val
        if len(time_val_list) == 0:
            minimum_time_val_seconds = 0
        else:
            minimum_time_val_seconds = min(time_val_list)

        for wrapper_object in server_and_queue_wrapper_list:

            if wrapper_object.is_server:
                server_object = wrapper_object.server_object
                server_slot_list = server_object.server_slots

                if len(server_slot_list) > 0:
                    for customer in server_slot_list:
                        curr_val = customer.get_server_time()
                        deducted = curr_val - minimum_time_val_seconds

                        # override current duration with deducted val
                        customer.set_server_time(deducted)

        return minimum_time_val_seconds






