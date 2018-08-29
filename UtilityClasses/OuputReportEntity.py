class ReportEntity:

    def __init__(self):
        self.list_customer_system_time_seconds = []

    def add_sample(self, system_duration_seconds):
        self.list_customer_system_time_seconds.append(system_duration_seconds)