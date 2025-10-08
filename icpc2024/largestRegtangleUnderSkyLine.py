
t=int(input())
def findLargest(nums):
    stack=[]
    mxArea=0
    for i,num in enumerate(nums):
        start=i
        while stack and stack[-1][1] > num:
           index,h= stack.pop()
           mxArea=max(mxArea,h * (i-index))
           start-=1
        stack.append((start,num))
    for index, h in stack:
         n=len(nums)
         mxArea=max(mxArea,h * (n-index))
    return mxArea


for _ in range(t):
    nums=list(map(int,input().split(",")))
    res=findLargest(nums)
    print(res)