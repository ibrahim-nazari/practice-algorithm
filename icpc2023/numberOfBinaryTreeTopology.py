
t=int(input())
def factorial(n):
    res=1
    for i in range(1,n+1):
        res *=i
    return res
for _ in range(t):
    n=int(input())
    res=factorial(2 * n)/(factorial(n+1)* factorial(n))
    print(int(res))
