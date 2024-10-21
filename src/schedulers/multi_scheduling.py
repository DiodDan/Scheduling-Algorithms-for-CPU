from src.schedulers.fcfs import FcFsScheduler
from src.metric import Metric
from src.process import Process
from src.schedulers.round_robin import RoundRobin
from src.schedulers.scheduler_interface import SchedulerInterface


class MultilevelQueueScheduling(SchedulerInterface):
    def __init__(self, processes: list[Process] = None, time_quantum: int = 4):
        super().__init__(processes)
        self.time_quantum = time_quantum

        # Two queues: High-priority (Queue 1) uses Round Robin, Low-priority (Queue 2) uses FCFS
        self.queue1 = []  # High-priority processes (Round Robin)
        self.queue2 = []  # Low-priority processes (FCFS)

    def schedule(self) -> Metric:
        self.queue1 = []
        self.queue2 = []
        for process in self.processes:
            if process.priority <= 5:
                self.queue1.append(process)  # High-priority queue
            else:
                self.queue2.append(process)  # Low-priority queue

        # apply Round Robin on high priority queue
        metric1: Metric = RoundRobin(self.queue1, self.time_quantum).schedule()

        # apply FCFS on low priority queue
        metric2: Metric = FcFsScheduler(self.queue2).schedule()

        return metric2 + metric1

if __name__ == '__main__':
    scheduler = MultilevelQueueScheduling()
    metric = scheduler.schedule()
    print(*scheduler.processes, sep='\n')
    metric.calculate_metrics()
    print(metric)
