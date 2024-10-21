from typing import override

from src.schedulers.scheduler_interface import SchedulerInterface
from src.metric import Metric


class FcFsScheduler(SchedulerInterface):
    @override
    def schedule(self) -> Metric:
        self.processes.sort(key=lambda x: x.arrival_time)
        current_time = 0
        total_waiting_time: int = 0
        total_turnaround_time: int = 0
        total_burst_time: int = 0

        for process in self.processes:
            if process.arrival_time > current_time:
                current_time = process.arrival_time

            process.start_time = current_time
            process.completion_time = process.start_time + process.burst_time
            total_turnaround_time += process.calculate_turnaround_time()
            total_waiting_time += process.calculate_waiting_time()
            total_burst_time += process.burst_time
            current_time = process.completion_time

        return Metric(total_turnaround_time=total_turnaround_time,
                      total_waiting_time=total_waiting_time,
                      total_time=current_time,
                      total_burst_time=total_burst_time,
                      processes_amount=len(self.processes)
                      )


if __name__ == '__main__':
    scheduler = FcFsScheduler()
    metric = scheduler.schedule()
    print(*scheduler.processes, sep='\n')
    metric.calculate_metrics()
    print(metric)
