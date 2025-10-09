
t=int(input())
def minuteFormat(number):
    ft=number
    if number <=9:
        ft=f"0{number}"
    return ft
def hourFormat(number):
    ft=number
    ext='am'
    if number==12:
        ext='pm'
    if number==0:
        ft=f"{12}"
    elif number <=9:
        ft=f"0{number}"
    elif number > 12:
        ft=f"{number -12}"
        ext='pm'
    return [ft,ext]

for _ in range(t):
    n=int(input())
    times=[]
    for i in range(n):
        h,min=list(map(str.strip, input().split(":")))
        h=int(h)
        extension=None
        if len(min)>2 and (min[-2:]=="am" or min[-2:]=='pm'):
            extension=min[-2:]
            min= min[:-2]
        times.append([h,int(min),extension])
    result=[]
    for time in times:
        h,min,ext=time
        min=minuteFormat(min)
        h,extformat=hourFormat(h)
        result.append(f"{h}:{min}{extformat}")
    for rs in result:
        print(rs)
