



def findPattern(pattern,string):
    count_x=pattern.count('x')
    count_y=len(pattern)-count_x
    print(count_x)
    print(count_y)

    # if count_y==0
    length_string=len(string)
    if count_y==0:
        if length_string % count_x !=0:
             return [] # not possible
        length_x= length_string // count_x
        s1=string[:length_x]
        return [s1,""]
    if count_x==0:
        if length_string % count_y !=0:
            return [] # not possible
        length_y=length_string // count_y
        s2=string[:length_y]
        return ["",s2]
    for length_x in range(length_string // count_x, 0,-1):
        remain_length= length_string - (count_x * length_x)
        if remain_length <= 0 or   remain_length % count_y !=0:
            continue
        length_y= remain_length // count_y
        pos=0
        s1=None
        s2=None
        valid=True

        for char in pattern:
            if char=="x":
                sub=string[pos:pos + length_x]
                if s1 is None:
                    s1=sub
                elif s1 !=sub:
                    valid=False
                    break
                pos +=length_x
            else:
                sub=string[pos:pos+length_y]
                if s2 is None:
                    s2=sub
                elif s2 !=sub:
                    valid=False
                    break
                pos +=length_y
        if valid==True and s1 !=s2:
            result=[s1,s2]
            return result
    return []




# input example
# xyxy // pattern
# powerrangergopowerrangergo // string

pattern=input().strip()
string=input().strip()
res=findPattern(pattern,string)
print(" ".join(res))