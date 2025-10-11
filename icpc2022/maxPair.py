t=int(input())
for _ in range(t):
    n,mod=map(int,input().split())
    nums=list(map(int,input().split()))
    maxvalue=0
    for i in range(n):
        for j in range(n):
            calc= nums[i]+nums[j] + ((nums[i] - nums[j]) % mod)
            maxvalue=max(maxvalue,calc)
    print(maxvalue)