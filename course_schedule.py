n=2
prerequisites=[[1,0]]

prereq={ c:[] for c in range(n)}
for crs ,pre in prerequisites:
    prereq[crs].append(pre)
visit=set()
cycle=set()
output=[]

def dfs(c):
    if c in cycle:
        return False
    if c in visit:
        return True
    cycle.add(c)
    for ne in prereq[c]:
        if dfs(ne)==False:
            return False
    cycle.remove(c)
    visit.add(c)
    output.append(c)
    return True

for c in range(n):
    if dfs(c)==False:
        print([])
print(output)
