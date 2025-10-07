







def main():
    t=int(input())
    results=[]
    for i in range(t):

        n=int(input())
        start_times= list(map(int,input().split(" ")))
        finish_times= list(map(int,input().split(" ")))
        events=[]
        for i in range(n):
            events.append((start_times[i],"start"))
            events.append((finish_times[i],"end"))
        events.sort(key=lambda x:(x[0],x[1]=="start"))
        current_cpc=0
        max_cpu=0
        for event in events:
            if event[1]=="start":
                current_cpc +=1
                max_cpu=max(max_cpu,current_cpc)
            else:
                current_cpc -=1
        results.append(max_cpu)
    
    for result in results:
        print(result)









if __name__ =="__main__":
    main()