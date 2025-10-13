
nt,ntasks=map(int,input().split())
taskdata=[[] for _ in range(ntasks)]
for _ in range(nt):
    tasks=input().split()
    n=len(tasks)
    index=0
    for i in range(0,n,2):
        sign=tasks[i]
        attempt=tasks[i+1]
        taskdata[index].append((sign,attempt))
        index+=1
for task in taskdata:
    teamSolved=0
    teamAttempt=0
    incorrectAttempt=0
    for info in task:
        sign,att=info[0],int(info[1])
        if sign =="+":
            teamSolved+=1
            teamAttempt+=1
        else:
            if att !=0:
                teamAttempt+=1
        incorrectAttempt +=att
    print(teamSolved,teamAttempt,incorrectAttempt)
        
