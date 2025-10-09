from collections import defaultdict
from collections import Counter
n=int(input())
adj=defaultdict(list)
for i in range(n):
    items=input().strip().split(">")
    for i,item in enumerate(items):
        if not adj[item]:
           adj[item]=[]
        if i+1 < len(items):
           adj[item].append(items[i+1])
result={}
for char in adj:
    items=adj[char]
    objCounter=Counter(items)
    
    result[char]=sorted(objCounter.items(),key=lambda x: (-x[1], x[0]))
for rs in result:
    print(f"{rs}:{",".join(list(map(lambda x: str(x[0]),result[rs])))}")



