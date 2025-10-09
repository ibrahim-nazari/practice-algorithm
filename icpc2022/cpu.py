import heapq
t=int(input())
def findMinimumCpu(intervals):
    stack=[]
    intervals=list(intervals)
    intervals.sort()
    for i in range(len(intervals)):
        s,e=intervals[i]
        if stack and stack[0] <=s:
            heapq.heappop(stack)
        heapq.heappush(stack,e)
    return len(stack)


for _ in range(t):
    n=int(input())
    starts=list(map(int,input().split()))
    finishes=list(map(int,input().split()))
    intervals=zip(starts,finishes)
    res=findMinimumCpu(intervals)
    print(res)