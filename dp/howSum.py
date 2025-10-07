
# def howSum(targetSum,numbers):
#     if targetSum==0:return []
#     if targetSum <0:return None

#     for n in numbers:
#         remainder=targetSum - n
#         combination= howSum(remainder,numbers)
#         if combination !=None:
#             combination.append(n)
#             return combination
#     return None



# result=howSum(17,[4,10,7])
# print("result ----",result)

def howSumTabulation(target,numbers):
    table=[None] * (target + 1)
    table[0]=[]

    for i in range(target +1):
        current=table[i]
        if(current is not None):
            for n in numbers:
                if i+n <=target:
                    table[i+n]=table[i]+[n]
    return table[target]



result=howSumTabulation(17,[3,8,7])
print("result ---",result)


         

