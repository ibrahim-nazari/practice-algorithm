def laptop_rentals(test_cases):
    results = []
    
    for test_case in test_cases:
        n, intervals = test_case
        
        events = []
        for interval in intervals:
            start, end = interval
            events.append((start, 'start'))
            events.append((end, 'end'))
        
        # Sort events by time; prioritize 'end' events if times are equal
        events.sort(key=lambda x: (x[0], x[1] == 'start'))
        
        max_laptops = 0
        current_laptops = 0
        
        # Simulate the laptop rental process
        for event in events:
            if event[1] == 'start':
                current_laptops += 1
                max_laptops = max(max_laptops, current_laptops)
            else:
                current_laptops -= 1
        
        results.append(max_laptops)
    
    return results

# Input Parsing
def main():
    t = int(input())  # number of test cases
    test_cases = []
    
    for _ in range(t):
        n = int(input())  # number of intervals
        intervals = []
        for _ in range(n):
            s, e = map(int, input().split())
            intervals.append((s, e))
        test_cases.append((n, intervals))
    
    results = laptop_rentals(test_cases)
    
    # Output each result
    for result in results:
        print(result)

# Uncomment the line below to run the main function when providing input through console
main()
