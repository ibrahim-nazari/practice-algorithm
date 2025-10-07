
import heapq
def find_process_time(test_cases):
    result=[]
    for case in test_cases:
        counterN,customers=case["counterN"],case["customers"]
        counters=[0] * counterN
        heapq.heapify(counters)
        current_time=0

        for customer in customers:
            start,end=customer
            current_time +=start
            finish_time=heapq.heappop(counters)
            finish_time=max(finish_time,current_time)
            finish_time +=end
            heapq.heappush(counters,finish_time)
        result.append(max(counters))
    
    for rs in result:
        print(rs)






def main():
    T=int(input())
    test_cases=[]
    for _ in range(T):
       counterN,customerN=map(int,input().split())
       customers=[tuple(map(int,input().split())) for _ in range(customerN)]
       test_cases.append({"counterN":counterN,"customers":customers})
    
    find_process_time(test_cases)


if __name__ =="__main__":
    main()















































# import heapq

# def process_bank_queue(test_cases):
#     results = []
    
#     for test in test_cases:
#         C, N, customers = test['C'], test['N'], test['customers']
        
#         # Priority queue (min-heap) to keep track of the earliest available counter times
#         counters = [0] * C  # Initialize C counters with 0 processing time
#         heapq.heapify(counters)
        
#         current_time = 0
        
#         for arrival_time, process_time in customers:
#             # Fast forward the current time to the customer's arrival time
#             current_time += arrival_time
            
#             # Get the next available counter (the counter with the smallest finish time)
#             counter_finish_time = heapq.heappop(counters)
            
#             # Fast forward the counter's time if the current time is ahead
#             counter_finish_time = max(counter_finish_time, current_time)
            
#             # Add the processing time to this counter
#             counter_finish_time += process_time
            
#             # Push the updated counter time back to the heap
#             heapq.heappush(counters, counter_finish_time)
        
#         # The answer for this test case is the maximum time across all counters
#         results.append(max(counters))
    
#     return results

# # Reading input
# def read_input():
#     T = int(input())
#     test_cases = []
    
#     for _ in range(T):
#         C, N = map(int, input().split())
#         customers = [tuple(map(int, input().split())) for _ in range(N)]
#         test_cases.append({'C': C, 'N': N, 'customers': customers})
    
#     return test_cases

# def main():
#     test_cases = read_input()
#     results = process_bank_queue(test_cases)
    
#     for result in results:
#         print(result)

# if __name__ == "__main__":
#     main()
