from src.metric import Metric
from src.schedulers.scheduler_interface import SchedulerInterface


class PreemptivePriorityScheduling(SchedulerInterface):
    def schedule(self):
        current_time = 0
        ready_queue = []
        completed_processes = []
        total_turnaround_time = 0
        total_waiting_time = 0
        total_burst_time = sum(p.burst_time for p in self.processes)
        total_time = 0

        # Sort processes by arrival time initially
        self.processes.sort(key=lambda p: p.arrival_time)

        while len(completed_processes) < len(self.processes):
            # Add all processes that have arrived up to the current time to the ready queue
            for process in self.processes:
                if process.arrival_time <= current_time and process not in completed_processes and process not in ready_queue:
                    ready_queue.append(process)

            if not ready_queue:
                current_time += 1
                continue

            # Sort the ready queue by priority (higher priority processes first) and remaining time
            ready_queue.sort(key=lambda p: p.priority)

            current_process = ready_queue[0]

            # Execute for 1 time unit (preemption can happen at any time)
            if current_process.start_time is None:
                current_process.start_time = current_time

            current_process.remaining_time -= 1
            current_time += 1

            # If the process completes, record its completion time
            if current_process.remaining_time == 0:
                current_process.completion_time = current_time
                current_process.calculate_turnaround_time()
                current_process.calculate_waiting_time()
                completed_processes.append(current_process)
                ready_queue.remove(current_process)
                total_turnaround_time += current_process.turnaround_time
                total_waiting_time += current_process.waiting_time

        return Metric(total_turnaround_time=total_turnaround_time,
                      total_waiting_time=total_waiting_time,
                      total_time=current_time,
                      total_burst_time=total_burst_time,
                      processes_amount=len(self.processes)
                      )


if __name__ == '__main__':
    scheduler = PreemptivePriorityScheduling()
    metric = scheduler.schedule()
    print(*scheduler.processes, sep='\n')
    metric.calculate_metrics()
    print(metric)
