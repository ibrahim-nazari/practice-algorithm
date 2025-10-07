
from collections import Counter

def make_name(test_cases):

    result=[]
    for texts in test_cases:
        name1=texts[0]
        name2=texts[1]
        name1Count=Counter(name1)
        secondName=[]
        for c in name2:
            if c in name1Count and name1Count[c] !=0:
                name1Count[c] -=1
            else:
                secondName.append(c)
        result.append(f"{name1}{"".join(secondName)}")
    for rs in result:
        print(rs)









def main():
    T=int(input())
    test_cases=[]
    for i in range(T):
        text=input().split()
        test_cases.append(text)
    make_name(test_cases)


if __name__ =="__main__":
    main()