class ServerAndQueueWrapper:

    def __init__(self, queue_object=None, server_object=None):
        self.is_server = None
        self.queue_object = queue_object
        self.server_object = server_object

        if queue_object is None and server_object is None:
            raise RuntimeWarning("ServerAndQueueWrapper object instantiated without either a defined Server or "
                                 "PriorityQueue object")
        elif queue_object is not None and server_object is not None:
            raise RuntimeWarning("ServerAndQueueWrapper object instantiated with both a Server and PriorityQueue"
                                 "object instantiated.")
        else:
            if queue_object is None:
                self.is_server = True
            else:
                self.is_server = False





