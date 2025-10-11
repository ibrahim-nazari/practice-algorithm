t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    sets=[]
    setsLength=0
    for i in range(s):
        nums=list(map(int,input().split()))
        setsLength=nums[0]
        sets.append(nums[1:])
    resObject={}
    pattern=[0] * len(sets)
    for i in range(n):
        for x,item in enumerate(sets):
            pattern[x]=1 if i in item else 0
        if tuple(pattern) not in resObject:
          resObject[tuple(pattern)]=1
    print(len(resObject))




# 2
# 5 2
# 3 0 1 2
# 3 2 3 4
# 4 3
# 2 0 1
# 2 1 2
# 2 2 3