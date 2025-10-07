

# tabulation method
# def canSum(targetSum,numbers):
#     table=[False] * (targetSum + 1)
#     table[0]=True
#     for i in range(targetSum +1):
#         if table[i]==True:
#             for n in numbers:
#                 if i+n <=targetSum:
#                     table[i+n]=True
    
#     return table[targetSum]
    


# list1=[2,4,7]
# targetSum=16
# result=canSum(targetSum,list1)

# print("result ---",result)

# memoization method


def canSum(targetSum,numbers):
    if targetSum ==0:
        return True
    if targetSum < 0:
        return False
    
    for n in numbers:
        remainder=targetSum-n
        if canSum(remainder,numbers)==True:
            return True
    
    return False

result=canSum(16,[7,3,2])
print("result ---",result)



