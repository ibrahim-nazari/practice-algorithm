import heapq
t=int(input())
for _ in range(t):
    n=int(input())
    intervals=[list(map(int,input().split())) for _ in range(n)]
    intervals.sort()
    stack=[]
    for r in range(n):
        s,e=intervals[r]
        if stack and stack[0] < s:
            heapq.heappop(stack)
        heapq.heappush(stack,e)
    print(len(stack))