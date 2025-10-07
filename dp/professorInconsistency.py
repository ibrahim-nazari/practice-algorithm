def find_variance(marks):
    n=len(marks)
    mean=sum(marks)/n
    variance=sum((mark-mean) **2 for mark in marks)/n
    return variance


def  find_inconsistency(tcs):
    
    for professorsMarks in tcs:
        result=[]
        for marks in professorsMarks:
            variance=find_variance(marks)
            result.append(variance)
        
        max_variance=max(result)
        professorNth=result.index(max_variance) + 1
        print(f"{professorNth}\t{max_variance:.2f}")
        






def main():
    T=int(input())
    tcs=[]
    for _ in range(T):
        professorN=int(input())
        professorsMarks=[list(map(int,input().split(","))) for _ in range(professorN)]
        tcs.append(professorsMarks)
    find_inconsistency(tcs)


if __name__ =="__main__":
    main()
