import math
n=int(input().strip())
def isPrime(c):
    if c <=1:
        return False
    if c <=3:
        return True
    if c % 2 ==0:
        return False
    r=int(math.sqrt(c))
    for i in range(3,r+1 ,2):
        if i % 2==0:
            return False
    return True
    
if n<=3:
    print(-1)
else:
    b=n-2
    if isPrime(b):
        print(2,b)
    else:
        print(-1)


 
