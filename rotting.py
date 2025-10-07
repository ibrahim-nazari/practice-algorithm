# n=5
# 0 1
# 1 2
# 3 4
def findConnected(n,m,edges):
    par=[i for i in range(n)]
    rank=[1]*n
    def find(node):
        while node !=par[node]:
            par[node]=par[par[node]]
            node=par[node]
        return node
    def union(n1,n2):
        p1=find(n1)
        p2=find(n2)

        if p1==p2:
            return 0
        if rank[p1] > rank[p2]:
            par[p2]=p1
            rank[p1] +=rank[p2]
        else:
            par[p1]=p2
            rank[p2] +=rank[p1]
        return 1
    res=n
    for n1,n2 in edges:
        res -=union(n1,n2)
    return res
   
n=int(input())
m=int(input())
edges=[list(map(int,input().split())) for _ in range(m)]
res=findConnected(n,m,edges)
print(res)