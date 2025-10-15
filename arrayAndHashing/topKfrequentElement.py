from collections import Counter
nums=[1,1,1,2,2,3,4,4,4]
k=2
# output should [1,2]
freq=Counter(nums)
# freq (index:count)
sortedFrequentNums=sorted(freq.items(),key= lambda x: x[1],reverse=True)
res=[]
for i in range(k):
   res.append(sortedFrequentNums[i][0])
for rs in res:
   print(rs)