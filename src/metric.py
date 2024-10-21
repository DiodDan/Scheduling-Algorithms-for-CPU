class Metric:
    avg_waiting_time: float
    avg_turnaround_time: float
    cpu_utilization: float
    throughput: float

    def __init__(self,
                 total_turnaround_time: int,
                 total_waiting_time: int,
                 total_time: int,
                 total_burst_time: int,
                 processes_amount: int = 20):
        self.processes_amount = processes_amount
        self.total_turnaround_time = total_turnaround_time
        self.total_waiting_time = total_waiting_time
        self.total_time = total_time
        self.total_burst_time = total_burst_time


    def calculate_metrics(self) -> 'Metric':
        self.avg_waiting_time = self.total_waiting_time / self.processes_amount
        self.avg_turnaround_time = self.total_turnaround_time / self.processes_amount
        self.cpu_utilization = self.total_burst_time / self.total_time * 100
        self.throughput = self.processes_amount / self.total_time
        return self

    def __str__(self) -> str:
        return f"Average Waiting Time: {self.avg_waiting_time}\n" \
               f"Average Turnaround Time: {self.avg_turnaround_time}\n" \
               f"CPU Utilization: {self.cpu_utilization}%\n" \
               f"Throughput: {self.throughput}"

    def __add__(self, other):
        return Metric(self.total_turnaround_time + other.total_turnaround_time,
                      self.total_waiting_time + other.total_waiting_time,
                      self.total_time + other.total_time,
                      self.total_burst_time + other.total_burst_time,
                      self.processes_amount + other.processes_amount)