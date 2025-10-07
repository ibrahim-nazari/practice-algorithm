

def findMinimumRoom(tcs):
    for rooms in tcs:
        rooms.sort(key=lambda x: x[1])

        count=1
        last_end_time=rooms[0][1]
        for room in rooms:
            if room[0] > last_end_time:
                count +=1
                last_end_time=room[1]
        print(count)

def main():
    t=int(input())
    tcs=[]
    for _ in range(t):
        start_times=list(map(int,input().split(",")))
        finish_times=list(map(int,input().split(",")))
        meetings=[(start_times[i],finish_times[i]) for i in range(len(start_times))]
        tcs.append(meetings)
    findMinimumRoom(tcs)


main()