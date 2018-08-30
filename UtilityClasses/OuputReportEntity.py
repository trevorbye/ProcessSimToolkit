class ReportEntity:

    def __init__(self):
        self.list_customer_system_time_seconds = []

    def add_sample(self, system_duration_seconds):
        """
        Adds Customer-time-in-system to output object. This class is used for outputting sim data to visualizations.

        :param system_duration_seconds: Total seconds Customer spent in system.
        :type system_duration_seconds: float
        :return: void
        """
        self.list_customer_system_time_seconds.append(system_duration_seconds)