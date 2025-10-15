import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=-1
    
    for i in range(2,math.isqrt(n)+1):
        if n % i ==0:
            a=i
            break
    if a == -1:
        print("NO")
    else:
        b=-1
        c=-1
        n1=n//a
        for j in range(2, math.isqrt(n1)+1):
            if n1 % j==0:
                b=j
                c =n1//b
                if b !=a and c !=a and b !=c:
                    break
                else:
                    b=-1
                    c=-1
        if b != -1 :
            print("YES")
            print(a,b,c)
        else:
            print("NO")
