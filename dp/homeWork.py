
def calculateSumMultiple(tcases):
    for numbers in tcases:
        numberResult=[]
        for fn,sn in numbers:
            sum=fn + sn
            mul=fn * sn
            numberResult.append((sum,mul))
        for rs in numberResult:
             " ".join(map(str,rs))
            




def main():
    T=int(input())
    cases=[]
    for _ in range(T):
        n=int(input())
        numbers=[tuple(map(int,input().split())) for _ in range(n)]
        cases.append(numbers)
    calculateSumMultiple(cases)

if __name__ =="__main__":
    main()
         
