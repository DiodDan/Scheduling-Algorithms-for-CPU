### [👈 Back to README](../../README.md)

# Shortest Job First (SJF)

### SJF schedules processes based on the shortest burst time. It can be implemented in both preemptive and non-preemptive modes.

---

- # Non-Preemptive SJF:
  ## Description:
  ### The CPU selects the process with the shortest burst time, but once selected, the process cannot be interrupted until it finishes.

  ## Working:

  ### After a process finishes, the CPU looks for the process with the smallest burst time from the remaining ones.

  ## Python code:

  ### [🐍 Python code](../../src/schedulers/non_preemptive_sjf.py)

  ## Run example:

    ```text
    PID: 15, Arrival Time: 1, Burst Time: 12, Priority: 6
    PID: 5, Arrival Time: 3, Burst Time: 6, Priority: 8
    PID: 20, Arrival Time: 7, Burst Time: 9, Priority: 7
    PID: 9, Arrival Time: 8, Burst Time: 13, Priority: 4
    PID: 2, Arrival Time: 12, Burst Time: 11, Priority: 4
    PID: 8, Arrival Time: 14, Burst Time: 4, Priority: 5
    PID: 6, Arrival Time: 34, Burst Time: 11, Priority: 1
    PID: 16, Arrival Time: 34, Burst Time: 19, Priority: 6
    PID: 18, Arrival Time: 40, Burst Time: 12, Priority: 3
    PID: 10, Arrival Time: 45, Burst Time: 2, Priority: 2
    PID: 13, Arrival Time: 56, Burst Time: 11, Priority: 6
    PID: 19, Arrival Time: 56, Burst Time: 17, Priority: 3
    PID: 11, Arrival Time: 57, Burst Time: 4, Priority: 7
    PID: 17, Arrival Time: 62, Burst Time: 17, Priority: 6
    PID: 12, Arrival Time: 65, Burst Time: 12, Priority: 4
    PID: 4, Arrival Time: 66, Burst Time: 6, Priority: 2
    PID: 7, Arrival Time: 75, Burst Time: 18, Priority: 8
    PID: 3, Arrival Time: 84, Burst Time: 1, Priority: 7
    PID: 14, Arrival Time: 90, Burst Time: 18, Priority: 3
    PID: 1, Arrival Time: 95, Burst Time: 5, Priority: 6
    Average Waiting Time: 35.65
    Average Turnaround Time: 46.05
    CPU Utilization: 99.52153110047847%
    Throughput: 0.09569377990430622
    ```

  ## Advantages:
    - ### Minimizes average waiting time and turnaround time compared to FCFS.
  ## Disadvantages:
    - ### Non-preemptive SJF can cause starvation of longer processes if new short processes keep arriving.
    - ### Not suitable for real-time systems where response time is critical.

---

- # Preemptive SJF (also known as Shortest Remaining Time First or SRTF):
  ## Description:

  ### A preemptive version of SJF where the CPU can switch to a new process if it arrives with a shorter burst time than the current running process.

  ## Working:

  ### If a new process arrives with a burst time shorter than the remaining burst time of the currently running process, the CPU preempts the current process and runs the new one.
  
  ## Python code:
  ### [🐍 Python code](../../src/schedulers/preemptive_sjf.py)
  
  ## Run Example:
  ```text
  PID: 4, Arrival Time: 0, Burst Time: 5, Priority: 4
  PID: 20, Arrival Time: 20, Burst Time: 16, Priority: 6
  PID: 5, Arrival Time: 23, Burst Time: 9, Priority: 7
  PID: 1, Arrival Time: 27, Burst Time: 8, Priority: 5
  PID: 2, Arrival Time: 32, Burst Time: 3, Priority: 4
  PID: 7, Arrival Time: 34, Burst Time: 2, Priority: 5
  PID: 16, Arrival Time: 37, Burst Time: 15, Priority: 4
  PID: 3, Arrival Time: 39, Burst Time: 17, Priority: 8
  PID: 6, Arrival Time: 40, Burst Time: 11, Priority: 10
  PID: 14, Arrival Time: 45, Burst Time: 6, Priority: 3
  PID: 13, Arrival Time: 53, Burst Time: 18, Priority: 6
  PID: 12, Arrival Time: 57, Burst Time: 16, Priority: 5
  PID: 11, Arrival Time: 58, Burst Time: 7, Priority: 8
  PID: 10, Arrival Time: 59, Burst Time: 1, Priority: 9
  PID: 15, Arrival Time: 61, Burst Time: 16, Priority: 5
  PID: 19, Arrival Time: 66, Burst Time: 15, Priority: 3
  PID: 9, Arrival Time: 75, Burst Time: 6, Priority: 1
  PID: 17, Arrival Time: 87, Burst Time: 7, Priority: 7
  PID: 8, Arrival Time: 88, Burst Time: 3, Priority: 8
  PID: 18, Arrival Time: 96, Burst Time: 20, Priority: 2
  Average Waiting Time: 35.0
  Average Turnaround Time: 45.05
  CPU Utilization: 93.05555555555556%
  Throughput: 0.09259259259259259
  ```
  ## Advantages:

    - ### Reduces waiting time and improves CPU utilization.

  ## Disadvantages:

    - ### Can lead to more context switches, which slightly increases overhead.
    - ### Long processes may suffer from starvation.

---

# Comparison (Preemptive vs. Non-Preemptive SJF):

## Preemptive
### SJF gives higher priority to shorter processes even after a longer process starts, which reduces waiting time but can lead to higher context switch overhead.

## Non-preemptive
### SJF is simpler but can suffer from long waiting times for larger processes.