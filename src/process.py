from random import randint


class Process:
    def __init__(self, pid: int, arrival_time: int, burst_time: int, priority: int = 0):
        self.pid = pid  # Process ID
        self.arrival_time = arrival_time  # Time at which the process arrives
        self.burst_time = burst_time  # Time required for the process to complete
        self.priority = priority  # Priority of the process (for Priority Scheduling)
        self.remaining_time = burst_time  # Used in preemptive scheduling to track remaining time
        self.start_time = None  # Time when the process starts execution
        self.completion_time = None  # Time when the process finishes execution
        self.waiting_time = 0  # Time spent in the ready queue
        self.turnaround_time = 0  # Total time from arrival to completion

    def calculate_waiting_time(self) -> int:
        self.waiting_time = self.turnaround_time - self.burst_time
        return self.waiting_time

    def calculate_turnaround_time(self) -> int:
        if self.completion_time is not None:
            self.turnaround_time = self.completion_time - self.arrival_time
        return self.turnaround_time

    def __str__(self) -> str:
        return f"PID: {self.pid}, Arrival Time: {self.arrival_time}, Burst Time: {self.burst_time}, " \
               f"Priority: {self.priority}"

    @staticmethod
    def generate_processes(num_processes: int = 20) -> list['Process']:
        processes = []
        for i in range(num_processes):
            arrival_time = randint(0, 100)  # Random arrival time
            burst_time = randint(1, 20)  # Random burst time
            priority = randint(1, 10)  # Random priority for priority scheduling
            process = Process(i + 1, arrival_time, burst_time, priority)
            processes.append(process)
        return processes
