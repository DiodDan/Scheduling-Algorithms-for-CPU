from src.metric import Metric
from src.process import Process
from src.schedulers.scheduler_interface import SchedulerInterface


class RoundRobin(SchedulerInterface):
    def __init__(self, processes: list[Process] = None, time_quantum: int = 4):
        super().__init__(processes)
        self.time_quantum = time_quantum

    def schedule(self):
        current_time = 0
        ready_queue = []
        completed_processes = []
        total_turnaround_time = 0
        total_waiting_time = 0
        total_burst_time = sum(p.burst_time for p in self.processes)

        # Sort processes by arrival time
        self.processes.sort(key=lambda p: p.arrival_time)
        ready_queue.append(self.processes[0])  # Add first process

        while len(completed_processes) < len(self.processes):
            if ready_queue:
                current_process = ready_queue.pop(0)

                # Execute for a time quantum or until process finishes, whichever is less
                if current_process.start_time is None:
                    current_process.start_time = current_time

                execute_time = min(self.time_quantum, current_process.remaining_time)
                current_process.remaining_time -= execute_time
                current_time += execute_time

                # If process is finished, record its completion time
                if current_process.remaining_time == 0:
                    current_process.completion_time = current_time
                    current_process.calculate_turnaround_time()
                    current_process.calculate_waiting_time()
                    completed_processes.append(current_process)
                    total_turnaround_time += current_process.turnaround_time
                    total_waiting_time += current_process.waiting_time

                # Check for newly arrived processes
                for process in self.processes:
                    if process.arrival_time <= current_time and process not in completed_processes and process not in ready_queue:
                        ready_queue.append(process)
            else:
                # If ready queue is empty, move the current time forward
                current_time += 1
                for process in self.processes:
                    if process.arrival_time <= current_time and process not in completed_processes and process not in ready_queue:
                        ready_queue.append(process)

        total_time = current_time
        return Metric(total_turnaround_time=total_turnaround_time,
                      total_waiting_time=total_waiting_time,
                      total_time=total_time,
                      total_burst_time=total_burst_time,
                      processes_amount=len(self.processes)
                      )


if __name__ == '__main__':
    scheduler = RoundRobin()
    metric = scheduler.schedule()
    print(*scheduler.processes, sep='\n')
    metric.calculate_metrics()
    print(metric)
