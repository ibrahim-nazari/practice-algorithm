
from collections import defaultdict
def convert_to_digit(limit,text):
    dataMap=defaultdict(int)
    result=""
    placehoolder=1
    for i in range(0,len(text),limit):
        txt=text[i: i + limit]
        if txt  not in dataMap:
            dataMap[txt]=placehoolder
            placehoolder +=1
        result += str(dataMap[txt])
    print(result)
    


def main():
    T=int(input())

    for i in range(T):
        data=input().split()
        limit= int(data[0])
        text=data[1]
        convert_to_digit(limit,text)

main()