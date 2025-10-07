
# nth 7,9
# n -> (n-1) + (n-2)   

def fib(n):
    table=[0] *(n +1)
    table[1]=1
    for i in range(n):
        current=table[i]
        table[i +1] +=current
        if i+2 <=n: table[i +2] +=current
    return table[n]



result=fib(1)
print("result ---> ",result)