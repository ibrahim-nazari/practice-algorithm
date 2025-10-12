t=int(input())
for _ in range(t):
    s=input().strip()
    codes=set()
    count=0
    for i in range(len(s)-1):
        key=s[i:i+2]
        if key not in codes:
            codes.add(key)
            count +=1
    print(count)

