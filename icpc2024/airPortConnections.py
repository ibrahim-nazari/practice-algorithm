from collections import defaultdict
t=int(input())
def dfs(node,graph,visit):
    visit.add(node)
    for ne in graph[node]:
        if ne not in visit:
            dfs(ne,graph,visit)
def findMinConnection(airports,edges,start):
    # find reachable airports
    visit=set()
    graph=defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
    dfs(start,graph,visit)

    # find unreachable
    unreachable=[a for a in airports if a not in visit]
    if not unreachable:
        return 0

    # strongly connected component
    connection_map={}
    for airport in unreachable:
        new_visit=set()
        dfs(airport,graph,new_visit)
        connection_map[airport]=[a for a in new_visit if a not in visit]
    # sort unreachable decendengly
    decendent_unreachable=sorted(unreachable,key=lambda x: len(connection_map[x]),reverse=True)
    connection_need=0
    reached=set(visit)
    for airport in decendent_unreachable:
        if airport in reached:
            continue
        connection_need +=1
        for a in connection_map[airport]:
            reached.add(a)
    return connection_need



    #  2 connecting strongly connected component result
for _ in range(t):
    airports=input().strip().split(",")
    nroutes=int(input())
    edges=[tuple(input().strip().split(",")) for _ in range(nroutes)]
    start=input().strip()
    res=findMinConnection(airports,edges,start)
    print(res)

# sample input
# 1 
# BGI,CDG,DEL,DOH,DSM,EWR,EYW,HND,ICN,JFK,LGA,LHR,ORD,SAN,SFO,SIN,TLV,BUD 
# 19
# DSM,ORD
# ORD,BGI
# BGI,LGA
# SIN,CDG 
# CDG,SIN
# CDG,BUD
# DEL,DOH
# DEL,CDG
# TLV,DEL
# EWR,HND 
# HND,ICN 
# JFK,LGA
# EYW,LHR
# LHR,SFO
# SFO,SAN
# SFO,DSM
# SAN,EYW
# LGA