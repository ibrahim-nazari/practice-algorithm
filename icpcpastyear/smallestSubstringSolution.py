t=int(input())
def find_max_overlap(s1,s2):
    max_over_lap=0
    combined_string=s1+s2
    minLen=min(len(s1),len(s2))+ 1
    for i in range(1,minLen):
        if s1[-i:]==s2[:i]:
            max_over_lap=i
            combined_string=s1+s2[i:]
    for i in range(1,minLen):
        if s2[-i:]==s1[:i]:
            if max_over_lap < i:
               max_over_lap=i
               combined_string=s2+s1[i:]
    return combined_string, max_over_lap



def findSmallestSubstring(strings):
    while len(strings) > 1:
        max_len=-1
        best_pair=(0,1)
        new_string=""
        for i in range(len(strings)):
            for j in range(i+1,len(strings)):
                combined,over_lap=find_max_overlap(strings[i],strings[j])
                if over_lap >  max_len:
                    best_pair=(i,j)
                    new_string =combined
                    max_len=over_lap
        i,j=best_pair
        strings[i]=new_string
        strings.pop(j)
    return strings[0]
for _ in range(t):
    strings=input().strip().split(",")
    res=findSmallestSubstring(strings)
    print(res)