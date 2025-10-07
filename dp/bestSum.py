# def bestSum(targetSum, numbers, memo=None):
#     if memo is None:
#         memo = {}  # Initialize memo if not provided
        
#     if targetSum in memo:
#         return memo[targetSum]

#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return None

#     shortResult = None

#     for n in numbers:
#         remainder = targetSum - n
#         combination = bestSum(remainder, numbers, memo)
#         if combination is not None:
#             # Create a new list by copying combination and adding n
#             new_combination = combination + [n]
#             if shortResult is None or len(new_combination) < len(shortResult):
#                 shortResult = new_combination
    
#     memo[targetSum] = shortResult
#     return shortResult


# result = bestSum(16, [2, 4, 8, 10])
# print("result ----> ", result)

def bestSumTabulation(target,numbers):
    table=[None] * (target + 1)
    table[0]=[]

    for i in range(target + 1):
        current=table[i]
        if current is not None:

            for n in numbers:
                if i + n <=target:
                    feild=table[i+n]
                    newFeild=table[i]+[n]
                    if feild is  None or len(feild) > len(newFeild):
                        table[i+n]=newFeild
    return table[target]
    



result=bestSumTabulation(8,[2,3,5])

print("result ---> ",result)



