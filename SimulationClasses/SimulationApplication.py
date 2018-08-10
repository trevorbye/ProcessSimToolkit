import datetime
from SimulationClasses.EventStepperEntity import EventStepper


class SimApplication:

    # time params are Datetime objects
    def __init__(self, start_time, end_time, runs, server_and_queue_wrapper_list):
        self.start_time = start_time
        self.end_time = end_time
        self.runs = runs
        self.server_and_queue_wrapper_list = server_and_queue_wrapper_list
        self.sim_clock = start_time

    def run_sim(self):

        # primary sim loop
        for run in range(self.runs):

            # reset sim clock each run
            self.sim_clock = self.start_time

            while self.sim_clock < self.end_time:
                # run EventStepper to find time increment value in seconds
                step_val_seconds = EventStepper.evaluate_time_steps(self.server_and_queue_wrapper_list)
                time_delta = datetime.timedelta(seconds=step_val_seconds)

                # step sim clock
                self.sim_clock = self.sim_clock + time_delta

                # process all Customers in Servers/Queues








