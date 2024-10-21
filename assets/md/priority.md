### [👈 Back to README](../../README.md)

# Priority Scheduling

### In Priority Scheduling, each process is assigned a priority, and the CPU selects the process with the highest priority. This can be implemented in both preemptive and non-preemptive modes.

---

# Non-Preemptive Priority Scheduling:

## Description:

### The CPU selects the process with the highest priority and runs it to completion, then selects the next highest priority process.

## Working:

### If two processes have the same priority, they are scheduled based on arrival time (FCFS).

## Python code:

### [🐍 Python code](../../src/schedulers/non_preemprive_priority_scheduling.py)

## Run example:

```text
PID: 5, Arrival Time: 1, Burst Time: 6, Priority: 3
PID: 16, Arrival Time: 7, Burst Time: 8, Priority: 9
PID: 15, Arrival Time: 15, Burst Time: 11, Priority: 7
PID: 2, Arrival Time: 34, Burst Time: 1, Priority: 2
PID: 3, Arrival Time: 34, Burst Time: 7, Priority: 8
PID: 10, Arrival Time: 41, Burst Time: 8, Priority: 10
PID: 20, Arrival Time: 46, Burst Time: 5, Priority: 5
PID: 9, Arrival Time: 48, Burst Time: 20, Priority: 1
PID: 12, Arrival Time: 49, Burst Time: 4, Priority: 6
PID: 8, Arrival Time: 63, Burst Time: 18, Priority: 10
PID: 1, Arrival Time: 64, Burst Time: 12, Priority: 4
PID: 19, Arrival Time: 68, Burst Time: 10, Priority: 7
PID: 18, Arrival Time: 70, Burst Time: 4, Priority: 1
PID: 17, Arrival Time: 71, Burst Time: 8, Priority: 1
PID: 11, Arrival Time: 73, Burst Time: 2, Priority: 6
PID: 14, Arrival Time: 78, Burst Time: 6, Priority: 6
PID: 6, Arrival Time: 81, Burst Time: 13, Priority: 9
PID: 13, Arrival Time: 93, Burst Time: 11, Priority: 10
PID: 4, Arrival Time: 94, Burst Time: 20, Priority: 5
PID: 7, Arrival Time: 96, Burst Time: 8, Priority: 8
Average Waiting Time: 30.35
Average Turnaround Time: 39.45
CPU Utilization: 95.28795811518324%
Throughput: 0.10471204188481675
```

## Advantages:

- ### High-priority tasks are completed first.

## Disadvantages:

- ### Like SJF, non-preemptive priority scheduling can cause starvation of lower-priority processes.

---

# Preemptive Priority Scheduling:

## Description:

### The CPU can preempt the currently running process if a new process with a higher priority arrives.

## Working:

### The CPU checks priorities whenever a new process arrives. If the new process has a higher priority than the currently running process, it preempts the current process.

## Python code:

### [🐍 Python code](../../src/schedulers/non_preemprive_priority_scheduling.py)

## Run example:

```text
PID: 19, Arrival Time: 2, Burst Time: 14, Priority: 8
PID: 5, Arrival Time: 8, Burst Time: 17, Priority: 7
PID: 7, Arrival Time: 14, Burst Time: 6, Priority: 2
PID: 15, Arrival Time: 16, Burst Time: 13, Priority: 5
PID: 4, Arrival Time: 17, Burst Time: 6, Priority: 8
PID: 11, Arrival Time: 18, Burst Time: 4, Priority: 1
PID: 2, Arrival Time: 24, Burst Time: 13, Priority: 2
PID: 3, Arrival Time: 28, Burst Time: 19, Priority: 7
PID: 12, Arrival Time: 28, Burst Time: 1, Priority: 1
PID: 17, Arrival Time: 38, Burst Time: 8, Priority: 1
PID: 9, Arrival Time: 39, Burst Time: 13, Priority: 2
PID: 6, Arrival Time: 44, Burst Time: 19, Priority: 7
PID: 13, Arrival Time: 45, Burst Time: 18, Priority: 9
PID: 14, Arrival Time: 47, Burst Time: 20, Priority: 6
PID: 8, Arrival Time: 48, Burst Time: 17, Priority: 9
PID: 10, Arrival Time: 63, Burst Time: 14, Priority: 4
PID: 1, Arrival Time: 75, Burst Time: 2, Priority: 3
PID: 16, Arrival Time: 83, Burst Time: 5, Priority: 8
PID: 20, Arrival Time: 84, Burst Time: 10, Priority: 2
PID: 18, Arrival Time: 94, Burst Time: 15, Priority: 1
Average Waiting Time: 65.25
Average Turnaround Time: 76.95
CPU Utilization: 99.15254237288136%
Throughput: 0.0847457627118644
```

## Advantages:

- ### Ensures that high-priority processes always run as soon as possible.

## Disadvantages:

- ### Can result in a large number of context switches, increasing overhead.
- ### Can cause starvation of low-priority processes unless priority aging is used (where the priority of waiting processes is gradually increased).

---

# Comparison (Preemptive vs. Non-Preemptive Priority Scheduling):

## Preemptive Priority

### Scheduling responds faster to high-priority tasks at the cost of context switch overhead.

## Non-preemptive Priority

### Scheduling has lower overhead but is less responsive to newly arriving high-priority tasks.