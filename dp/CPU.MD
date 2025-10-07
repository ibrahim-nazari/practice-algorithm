This problem can be solved using the concept of interval scheduling and greedy algorithms. The goal is to find the minimum number of CPUs required to handle all background tasks without overlapping tasks assigned to the same CPU.

### Problem Breakdown:

- We need to find the number of CPUs required to handle tasks, where each task has a start time and a finish time.
- The tasks cannot overlap on the same CPU.
- We can think of this as an interval problem where we must determine how many intervals (tasks) overlap at any given time.

### Approach:

1. **Sorting Events:** First, break down each task into two events: a start event and a finish event. We'll then sort these events.
   - Each start event will increase the number of active tasks.
   - Each finish event will decrease the number of active tasks.
2. **Tracking CPU Usage:** We track the number of CPUs being used at each moment as we process the events. The maximum number of overlapping tasks at any point in time gives us the minimum number of CPUs needed.

### Steps:

1. For each test case:
   - Parse the start and finish times of the tasks.
   - Create a list of events (start and finish times).
   - Sort these events. When sorting, in case of a tie, process finish times before start times to ensure a task finishes before a new one starts at the same time.
   - Simulate the process by iterating through the events, counting how many tasks are active at the same time.
   - Keep track of the maximum number of active tasks (this will be the number of CPUs needed).
2. Output the maximum number of CPUs required for each test case.

### Solution Code (in Python):

```python
def min_cpus_needed(cases):
    results = []
    for _ in range(cases):
        T = int(input())  # Number of tasks
        start_times = list(map(int, input().split()))  # Start times
        finish_times = list(map(int, input().split()))  # Finish times

        events = []

        # Create a list of start and finish events
        for i in range(T):
            events.append((start_times[i], 'start'))
            events.append((finish_times[i], 'finish'))

        # Sort the events by time, with 'finish' before 'start' if times are the same
        events.sort(key=lambda x: (x[0], x[1] == 'start'))

        max_cpus = 0
        current_cpus = 0

        # Process the events
        for event in events:
            if event[1] == 'start':
                current_cpus += 1
                max_cpus = max(max_cpus, current_cpus)
            else:
                current_cpus -= 1

        results.append(max_cpus)

    # Output the result for each case
    for result in results:
        print(result)

# Read number of cases
cases = int(input())
min_cpus_needed(cases)
```

### Explanation:

- **Event Processing:** The algorithm processes both start and finish events. Whenever a task starts, it increments the count of active tasks (CPUs in use). When a task finishes, it decrements the count.
- **Sorting:** We sort the events by time. If two events have the same time, the 'finish' event is processed before the 'start' event to ensure that tasks do not overlap at the exact same time.
- **Complexity:** Sorting the events takes \(O(T \log T)\) for each test case, where \(T\) is the number of tasks. Processing the events takes \(O(T)\). Hence, the overall time complexity per test case is \(O(T \log T)\).

### Example Walkthrough:

For the input:

```
2
7
1 3 2 0 5 8 11
3 4 5 7 9 10 12
5
1 3 5 6 8
5 6 8 8 9
```

The output will be:

```
3
2
```

#### Explanation:

- **First case:** The maximum number of overlapping tasks is 3 (at times 2-3).
- **Second case:** The maximum number of overlapping tasks is 2 (at time 5-6).
