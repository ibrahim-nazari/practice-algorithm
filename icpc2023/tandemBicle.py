t=int(input())
for _ in range(t):
    reds=list(map(int,input().split(",")))
    blues=list(map(int,input().split(",")))
    fastest=input().strip().lower()=="true"
    reds.sort()
    if fastest:
        blues.sort(reverse=True)
    else:
        blues.sort()
    res=0
    for red,blue in  zip(reds,blues):
        res +=max(red,blue)
    print(res)
