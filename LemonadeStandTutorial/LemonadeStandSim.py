from UtilityClasses.ServerEntity import Server
from UtilityClasses.QueueEntity import PriorityQueue
from UtilityClasses.TimeRandomizerEntity import TimeRandomizer
from UtilityClasses.ServerAndQueueWrapperEntity import ServerAndQueueWrapper

from SimulationClasses.SimulationApplication import SimApplication

import datetime

# build wrapper list. After you create each Server/Queue, wrap it in ServerAndQueueWrapper and add to this list
server_queue_wrapper_list = []

# build arrival server
# build time randomizer
arrival_time_randomizer = TimeRandomizer("normal", normal_mean=20, normal_stddev=5)

# build server using randomizer. Capacity should always = 1 for arrival server
arrival_server = Server(1, arrival_time_randomizer, description="Arrival Server")

# wrap server and add to list
arrival_wrapper = ServerAndQueueWrapper(server_object=arrival_server)
server_queue_wrapper_list.append(arrival_wrapper)


# build Queue (line), Customers will be input into Queue after they are instantiated into system by the arrival server.
arrival_queue = PriorityQueue(description="Lemonade Stand Line")

# wrap Queue and add to list
queue_wrapper = ServerAndQueueWrapper(queue_object=arrival_queue)
server_queue_wrapper_list.append(queue_wrapper)


# build main process Server (serving Customers lemonade)
# build time randomizer
main_process_randomizer = TimeRandomizer("triangular", triangle_min=30, triangle_mode=40, triangle_max=70)

# build process server, assume there are two employees serving lemonade to customers
main_process_server = Server(4, main_process_randomizer, "Main process Server (serving Lemonade)")

# wrap server and add to list
main_process_wrapper = ServerAndQueueWrapper(server_object=main_process_server)
server_queue_wrapper_list.append(main_process_wrapper)


# Configuration for Sim
start_time = datetime.datetime(year=2018, month=7, day=1, hour=12, minute=0, second=0)
end_time = datetime.datetime(year=2018, month=7, day=2, hour=12, minute=0, second=0)

# create sim object, specify number of runs, specify True/False for histogram plot
sim = SimApplication(start_time, end_time, 500, server_queue_wrapper_list,
                     output_plot=True, mean_stabilization_tracking=True)

# run configured setup
sim.run_sim()
