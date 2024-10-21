### [👈 Back to README](../../README.md)

# Round Robin (RR)

## Description:

### Round Robin (RR) is a preemptive scheduling algorithm where each process gets an equal share of the CPU time, defined by a time quantum.

## Working:

### The CPU cycles through the processes in a circular queue. Each process runs for a maximum of one time quantum and is then preempted and sent to the back of the queue if it hasn’t finished.

## Python code:

### [🐍 Python code](../../src/schedulers/non_preemptive_sjf.py)

## Run example:

```text
PID: 14, Arrival Time: 5, Burst Time: 3, Priority: 7
PID: 5, Arrival Time: 13, Burst Time: 3, Priority: 3
PID: 7, Arrival Time: 23, Burst Time: 4, Priority: 9
PID: 1, Arrival Time: 25, Burst Time: 6, Priority: 4
PID: 17, Arrival Time: 29, Burst Time: 17, Priority: 2
PID: 16, Arrival Time: 39, Burst Time: 15, Priority: 10
PID: 11, Arrival Time: 42, Burst Time: 6, Priority: 10
PID: 4, Arrival Time: 48, Burst Time: 19, Priority: 3
PID: 15, Arrival Time: 63, Burst Time: 10, Priority: 5
PID: 18, Arrival Time: 68, Burst Time: 12, Priority: 3
PID: 10, Arrival Time: 69, Burst Time: 6, Priority: 2
PID: 6, Arrival Time: 71, Burst Time: 6, Priority: 10
PID: 20, Arrival Time: 74, Burst Time: 14, Priority: 8
PID: 3, Arrival Time: 77, Burst Time: 18, Priority: 7
PID: 2, Arrival Time: 85, Burst Time: 15, Priority: 1
PID: 19, Arrival Time: 88, Burst Time: 7, Priority: 8
PID: 8, Arrival Time: 89, Burst Time: 4, Priority: 9
PID: 13, Arrival Time: 90, Burst Time: 1, Priority: 2
PID: 9, Arrival Time: 94, Burst Time: 6, Priority: 7
PID: 12, Arrival Time: 95, Burst Time: 13, Priority: 4
Average Waiting Time: 52.35
Average Turnaround Time: 61.6
CPU Utilization: 91.58415841584159%
Throughput: 0.09900990099009901
```
## Advantages:

- ### Ensures fairness, as all processes get an equal share of CPU time.
- ### Good for time-sharing systems (like interactive systems) where response time is important.

## Disadvantages:

- ### Performance depends heavily on the choice of time quantum. If the quantum is too large, it behaves like FCFS; if too small, it leads to many context switches, increasing overhead.

## Example:

For a time quantum of 2 ms, if Process 1 has a burst time of 5 ms, it will get 2 ms, then be preempted, and run again after
other processes get their turns.