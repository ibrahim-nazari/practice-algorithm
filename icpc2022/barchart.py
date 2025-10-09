t=int(input())
for _ in range(t):
    data=input().strip().split()
    completedRow=int(data[0])
    L=data[1]
    def format(x):
        key,percent=x.split(":")
        return [str(key.strip()), int(percent)]
    bars=list(map(format , data[2:]))
    print(bars)
    for bar in bars:
        key,percent=bar
        cols= round(percent * completedRow/100)
        print(f"{key}:{str(L) * cols} {percent:.2f}")
