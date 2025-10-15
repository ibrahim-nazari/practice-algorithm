nums=[1,2,3,4]
# out put should [24,12,8,6]
prefixes=[]
prefix=1
for i in range(len(nums)):
    prefixes.append(prefix)
    prefix *= nums[i]
# [1,1,2,6]
sufix=1
result=[]
for i in range(len(nums)-1,-1,-1):
    num=sufix * prefixes[i]
    result.append(num)
    sufix *=nums[i]
result.reverse()
for rs in result:
    print(rs)
