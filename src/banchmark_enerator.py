import matplotlib.pyplot as plt
import numpy as np

from src.metric import Metric
from src.schedulers import (
    MultilevelQueueScheduling,
    NonPreemptivePriorityScheduling,
    NonPreemptiveSJFScheduler,
    PreemptivePriorityScheduling,
    PreemptiveSJFScheduler,
    RoundRobin,
    FcFsScheduler
)

schedulers = [
    MultilevelQueueScheduling(),
    NonPreemptivePriorityScheduling(),
    NonPreemptiveSJFScheduler(),
    PreemptivePriorityScheduling(),
    PreemptiveSJFScheduler(),
    RoundRobin(),
    FcFsScheduler()
]

plt.style.use('dark_background')

def open_metric(metric: Metric):
    return [metric.avg_waiting_time, metric.avg_turnaround_time, metric.cpu_utilization, metric.throughput]


metric_labels = ['Average Waiting Time', 'Average Turnaround Time', 'CPU Utilization', 'Throughput']
data = [open_metric(s.benchmark().calculate_metrics()) for s in schedulers]
data = np.array(data)
x = np.arange(len(metric_labels))
width = 0.1
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()
colors = plt.colormaps['tab20b_r']

for i, ax in enumerate(axes):
    for j, scheduler in enumerate(schedulers):
        ax.bar(x[i] + j * width, data[j, i], width, label=scheduler.__class__.__name__, color=colors(j))

    ax.set_xlabel('Metrics')
    ax.set_ylabel('Values')
    ax.set_title(metric_labels[i])
    ax.set_xticks(x + width * (len(schedulers) - 1) / 2)
    ax.set_xticklabels(metric_labels)
    ax.legend()

plt.tight_layout()

plt.grid(True)
plt.show()