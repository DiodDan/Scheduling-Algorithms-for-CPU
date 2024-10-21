from abc import ABC, abstractmethod

from src.metric import Metric
from src.process import Process


class SchedulerInterface(ABC):
    processes: list[Process] = []

    def __init__(self, processes: list[Process] = None):
        if processes is not None:
            self.processes = processes
        else:
            self.processes = Process.generate_processes()

    def benchmark(self) -> Metric:
        metric_sum = self.schedule()
        for _ in range(100):
            self.processes = Process.generate_processes()
            metric_sum += self.schedule()
        return metric_sum

    @abstractmethod
    def schedule(self): ...

