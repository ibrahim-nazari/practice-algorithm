def elevator_sequence(requests):
    # Determine initial direction
    current_floor = requests[0]
    direction = 'up' if requests[1] > requests[0] else 'down'
    
    # Separate floors into two groups: those above current floor and those below
    up_requests = sorted([floor for floor in requests if floor > current_floor])
    down_requests = sorted([floor for floor in requests if floor < current_floor], reverse=True)
    
    result = [current_floor]
    
    while up_requests or down_requests:
        if direction == 'up':
            # Serve all up requests first
            while up_requests:
                next_floor = up_requests.pop(0)
                result.append(next_floor)
            # If there are down requests, change direction
            if down_requests:
                direction = 'down'
        else:
            # Serve all down requests first
            while down_requests:
                next_floor = down_requests.pop(0)
                result.append(next_floor)
            # If there are up requests, change direction
            if up_requests:
                direction = 'up'
    
    return result


# Input processing and output
def main():
    # Number of test cases
    N = int(input())
    
    for _ in range(N):
        requests = list(map(int, input().split()))
        result = elevator_sequence(requests)
        print(" ".join(map(str, result)))


# Example usage
if __name__ == "__main__":
    main()
