### [👈 Back to README](../../README.md)



# First-Come, First-Served (FCFS)

## Description:

### FCFS is the simplest scheduling algorithm. Processes are executed in the order of their arrival. It’s non-preemptive, meaning once a process starts, it runs to completion without being interrupted.

## Working:

### The CPU picks the process that arrives first and runs it until it finishes, then picks the next process in the queue.

## Python code:

### [🐍 Python code](../../src/schedulers/fcfs.py)


## Run example:

```text
PID: 20, Arrival Time: 4, Burst Time: 20, Priority: 7
PID: 7, Arrival Time: 13, Burst Time: 1, Priority: 6
PID: 5, Arrival Time: 20, Burst Time: 6, Priority: 7
PID: 2, Arrival Time: 21, Burst Time: 19, Priority: 3
PID: 6, Arrival Time: 21, Burst Time: 12, Priority: 7
PID: 9, Arrival Time: 23, Burst Time: 6, Priority: 5
PID: 12, Arrival Time: 26, Burst Time: 2, Priority: 6
PID: 19, Arrival Time: 41, Burst Time: 15, Priority: 9
PID: 10, Arrival Time: 42, Burst Time: 3, Priority: 3
PID: 15, Arrival Time: 50, Burst Time: 2, Priority: 9
PID: 16, Arrival Time: 55, Burst Time: 6, Priority: 7
PID: 13, Arrival Time: 59, Burst Time: 2, Priority: 4
PID: 14, Arrival Time: 60, Burst Time: 13, Priority: 9
PID: 3, Arrival Time: 61, Burst Time: 7, Priority: 8
PID: 18, Arrival Time: 63, Burst Time: 2, Priority: 3
PID: 8, Arrival Time: 64, Burst Time: 16, Priority: 8
PID: 1, Arrival Time: 66, Burst Time: 14, Priority: 5
PID: 17, Arrival Time: 71, Burst Time: 1, Priority: 1
PID: 11, Arrival Time: 83, Burst Time: 5, Priority: 1
PID: 4, Arrival Time: 84, Burst Time: 2, Priority: 9
Average Waiting Time: 40.3
Average Turnaround Time: 48.0
CPU Utilization: 97.46835443037975%
Throughput: 0.12658227848101267
```


## Advantages:

- Simple to implement.
- Easy to understand.

## Disadvantages:

- Leads to the convoy effect, where short processes get stuck waiting for a long-running process.
- Not optimal for minimizing waiting time.
