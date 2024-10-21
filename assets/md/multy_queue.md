### [👈 Back to README](../../README.md)

# Multilevel Queue Scheduling

## Description:

### In Multilevel Queue Scheduling, processes are divided into different queues based on their type (e.g., system processes, interactive processes, batch processes). Each queue may have a different scheduling algorithm and priority level.

## Working:

### The CPU schedules processes based on the queue they are in. For example, system processes may have higher priority over batch processes. A fixed priority is given to each queue, and processes within a queue are scheduled using another algorithm (e.g., FCFS, Round Robin).

## Advantages:

## Python code (It creates a multilevel queue with 2 queues as described in the example section):

### [🐍 Python code](../../src/schedulers/multi_scheduling.py)

## Run example:

```text
PID: 1, Arrival Time: 59, Burst Time: 14, Priority: 7
PID: 2, Arrival Time: 64, Burst Time: 9, Priority: 1
PID: 3, Arrival Time: 30, Burst Time: 8, Priority: 5
PID: 4, Arrival Time: 87, Burst Time: 1, Priority: 5
PID: 5, Arrival Time: 53, Burst Time: 12, Priority: 8
PID: 6, Arrival Time: 95, Burst Time: 5, Priority: 3
PID: 7, Arrival Time: 44, Burst Time: 15, Priority: 1
PID: 8, Arrival Time: 32, Burst Time: 10, Priority: 1
PID: 9, Arrival Time: 0, Burst Time: 18, Priority: 9
PID: 10, Arrival Time: 6, Burst Time: 9, Priority: 3
PID: 11, Arrival Time: 55, Burst Time: 6, Priority: 2
PID: 12, Arrival Time: 49, Burst Time: 18, Priority: 8
PID: 13, Arrival Time: 8, Burst Time: 2, Priority: 1
PID: 14, Arrival Time: 37, Burst Time: 14, Priority: 8
PID: 15, Arrival Time: 42, Burst Time: 5, Priority: 1
PID: 16, Arrival Time: 81, Burst Time: 9, Priority: 4
PID: 17, Arrival Time: 30, Burst Time: 12, Priority: 10
PID: 18, Arrival Time: 78, Burst Time: 13, Priority: 9
PID: 19, Arrival Time: 79, Burst Time: 19, Priority: 6
PID: 20, Arrival Time: 91, Burst Time: 9, Priority: 10
Average Waiting Time: 11.1
Average Turnaround Time: 21.5
CPU Utilization: 86.30705394190872%
Throughput: 0.08298755186721991
```

- ### Effective in systems where processes can be clearly divided into different categories with varying scheduling requirements.
- ### Provides flexibility for different scheduling algorithms for different types of processes.

## Disadvantages:

- ### Can lead to starvation of processes in lower-priority queues if higher-priority queues dominate CPU time.
- ### Implementation complexity increases as more queues are added.

## Example:

### A system may have two queues: a high-priority queue for interactive tasks using Round Robin with a small time quantum, and a lower-priority queue for batch jobs using FCFS.
