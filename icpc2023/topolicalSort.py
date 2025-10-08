
t=int(input())
def findSort(jd,jobs):
    adj={j :[] for j in jobs}
    for j,d in jd:
        adj[j].append(d)
    res=[]
    visit={}
    def dfs(node):
        if node in visit:
            return visit[node]
        visit[node]=True
        for ne in adj[node]:
            if dfs(ne):return True
        visit[node]=False
        res.append(node)
        return False
    
    for job in jobs:
        if dfs(job):
            return "Impossible"
    res.reverse()
    return res
    


for _ in range(t):
    n=int(input())
    jd=[list(map(int,input().split())) for _ in range(n)]
    jobs=list(map(int,input().split(",")))
    res=findSort(jd,jobs)
    print(",".join(map(str,res)))