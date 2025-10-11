
class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self,node):
        while node !=self.parent[node]:
            node=self.parent[node]
        return node
    def union(self,v,u):
        p1=self.find(v)
        p2=self.find(u)
        if p1==p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2]=p1
            self.rank[p1] +=1
        else:
            self.parent[p1]=p2
            self.rank[p2] +=1
        return True

t=int(input())
for _ in range(t):
    p,r=map(int,input().split())
    def formatData():
        v,u,w=map(int,input().split())
        return (w,v,u)
    routes=[formatData() for _ in range(r)]
    total=sum(w for w,_,x in routes)
    routes.sort()
    dsu=DSU(p)
    mst_cost=0
    edge_used=0
    for w,v,u in routes:
     
        if dsu.union(v,u):
            mst_cost +=w
            edge_used ==1
            if edge_used == p-1:
                break
    print(total- mst_cost)

  
    

