from typing import override


from src.schedulers.scheduler_interface import SchedulerInterface
from src.metric import Metric


class NonPreemptiveSJFScheduler(SchedulerInterface):
    @override
    def schedule(self) -> Metric:
        # Sort processes by arrival time initially
        self.processes.sort(key=lambda p: p.arrival_time)

        current_time = 0
        completed_processes = []
        ready_queue = []

        total_turnaround_time = 0
        total_waiting_time = 0
        total_burst_time = sum(p.burst_time for p in self.processes)

        while len(completed_processes) < len(self.processes):
            # Add processes to the ready queue which have arrived by current_time
            for process in self.processes:
                if process.arrival_time <= current_time \
                        and process not in ready_queue \
                        and process not in completed_processes:
                    ready_queue.append(process)

            # If the ready queue is empty, move time forward
            if not ready_queue:
                current_time += 1
                continue

            # Select the process with the shortest burst time
            ready_queue.sort(key=lambda p: p.burst_time)
            current_process = ready_queue.pop(0)

            # Execute the selected process
            if current_process.start_time is None:
                current_process.start_time = current_time
            current_time += current_process.burst_time
            current_process.completion_time = current_time
            current_process.calculate_turnaround_time()
            current_process.calculate_waiting_time()

            # Add to completed processes
            completed_processes.append(current_process)
            total_turnaround_time += current_process.turnaround_time
            total_waiting_time += current_process.waiting_time

        total_time = current_time
        return Metric(total_turnaround_time=total_turnaround_time,
                      total_waiting_time=total_waiting_time,
                      total_time=total_time,
                      total_burst_time=total_burst_time,
                      processes_amount=len(self.processes)
                      )


if __name__ == '__main__':
    scheduler = NonPreemptiveSJFScheduler()
    metric = scheduler.schedule()
    print(*scheduler.processes, sep='\n')
    metric.calculate_metrics()
    print(metric)
