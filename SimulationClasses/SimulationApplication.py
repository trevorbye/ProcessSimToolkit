import datetime
import numpy as np
from matplotlib import pyplot as plot
import copy

from SimulationClasses.EventStepperEntity import EventStepper
from SimulationClasses.InteractionLogicEntity import InteractionLogic
from UtilityClasses.OuputReportEntity import ReportEntity


class SimApplication:

    def __init__(self, start_time, end_time, runs, server_and_queue_wrapper_list, output_plot,
                 mean_stabilization_tracking):
        """
        Main container class for simulation. Accepts config and provides run() method.

        :param start_time: start of sim
        :type start_time: datetime.pyi
        :param end_time: end of sim
        :type end_time: datetime.pyi
        :param runs: number of times to run sim between start and end time
        :type runs: int
        :param server_and_queue_wrapper_list: list of ServerAndQueueWrapper objects
        :type server_and_queue_wrapper_list: list
        :param output_plot: include output plot
        :type output_plot: bool
        :param mean_stabilization_tracking: include mean stabilization plot
        :type mean_stabilization_tracking: bool
        """

        self.start_time = start_time
        self.end_time = end_time
        self.runs = runs
        self.server_and_queue_wrapper_list = server_and_queue_wrapper_list
        self.report_entity = None
        self.sim_clock = start_time
        self.output_plot = output_plot
        self.mean_stabilization_tracking = mean_stabilization_tracking

    def run_sim(self):
        # create report entity object to hold time-in-system values
        self.report_entity = ReportEntity()

        # used only for mean stabilization tracking
        means = []
        if self.mean_stabilization_tracking:
            plot.axis([0, self.runs, 0, 30])
            plot.title("Mean Stabilization of Total System Time")
            plot.xlabel("sim runs")
            plot.ylabel("mean")

        # primary sim loop
        for run in range(self.runs):
            # clean wrapper list for each new run, otherwise between runs you will end up with a customer left from the
            # previous run, resulting in a negative system duration being calculated
            wrapper_list_reset = copy.deepcopy(self.server_and_queue_wrapper_list)

            # initialize interaction logic object
            interaction_logic_processor = InteractionLogic(wrapper_list_reset, self.report_entity)

            # reset sim clock each run
            self.sim_clock = self.start_time

            while self.sim_clock < self.end_time:
                # run EventStepper to find time increment value in seconds
                step_val_seconds = EventStepper.evaluate_time_steps(wrapper_list_reset)

                if step_val_seconds > 0:
                    time_delta = datetime.timedelta(seconds=step_val_seconds)

                    # step sim clock
                    self.sim_clock = self.sim_clock + time_delta

                # process all Customers in Servers/Queues
                interaction_logic_processor.process_interactions(self.sim_clock)

            # update mean stabilization plot after each run
            if self.mean_stabilization_tracking:
                current_mean = (sum(self.report_entity.list_customer_system_time_seconds)
                                / float(len(self.report_entity.list_customer_system_time_seconds)))
                means.append(current_mean)
                current_x_pos = run + 1
                new_y_min = min(means)
                new_y_max = max(means)

                plot.scatter(current_x_pos, current_mean)
                plot.axis([0, self.runs, new_y_min, new_y_max])

                plot.pause(0.05)

        # print aggregated output
        print(self.report_entity.list_customer_system_time_seconds)

        # only plots if mean stabilization is not turned on
        if self.output_plot and not self.mean_stabilization_tracking:
            self.generate_output_plot(self.report_entity.list_customer_system_time_seconds)

    @staticmethod
    def generate_output_plot(time_list):
        """
        Plots output system time as histogram.

        :param time_list: List of system times from sim output
        :type time_list: list
        :return: void
        """

        list_as_ints = [int(i) for i in time_list]
        data = np.asarray(list_as_ints)

        plot.hist(data, edgecolor='black', linewidth=0.8, color="#08a32e")

        plot.title("Output: Seconds-in-system Distribution")
        plot.xlabel("bin")
        plot.ylabel("count")

        plot.show()
