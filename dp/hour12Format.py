

def time_format(time_str):
    if "am" in time_str or "pm" in time_str:
        times,peroids=time_str[:-2],time_str[-2:]
        hours,minutes=map(int,times.split(":"))
        return f'{hours:02}:{minutes:02}{peroids}'
    else:
        hours,minutes=map(int,time_str.split(":"))

        if hours==0:
            # it is 12 midnight
            return f'12:{minutes:02}am'
        elif hours==12:
            return f'12:{minutes:02}pm'
        elif hours > 12:
            return f'{hours -12:02}:{minutes:02}pm'
        else:
            return f'{hours:02}:{minutes:0}am'

def main():
    N=int(input())
    results=[]
    for i in range(N):
        results.append(time_format(input()))
    
    for result in results:
        print(result)

main()