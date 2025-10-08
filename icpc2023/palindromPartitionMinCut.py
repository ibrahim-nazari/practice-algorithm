t=int(input())
for _ in range(t):
    string=input().strip().lower()
 
    n=len(string)
    if n<=1:
        print(0)
    else:
        isPal=[[False] * n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if string[i]==string[j] and (j-i < 2 or isPal[i+1][j-1]):
                    isPal[i][j]=True
        cuts=[0] *n
        for i in range(n):
            if isPal[0][i]:
                cuts[i]=0
                continue
            best=i
            for j in range(1,i+1):
                if isPal[j][i]:
                    best=min(best,cuts[j-1]+1)
            cuts[i]=best
    print(cuts[-1])

