# def allConstruct(target, wordBank, memo=None):
#     if memo is None:
#         memo = {}
    
#     if target in memo:
#         return memo[target]
    
#     if target == '':
#         return [[]]  # Base case: one way to construct the empty string
    
#     result = []
    
#     for word in wordBank:
#         # If the word is a prefix of the target
#         if target.startswith(word):
#             suffix = target[len(word):]
#             # Recursive call for the remaining part of the target
#             suffixWays = allConstruct(suffix, wordBank, memo)
#             # Add the current word to the beginning of each way of constructing the suffix
#             targetWays = [[word] + way for way in suffixWays]
#             # Add all those ways to the result
#             result.extend(targetWays)
    
#     memo[target] = result
#     return result

# # Test example
# result = allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])
# print(result)


def allConstruct(text,wordBank):
    table=[None] * (len(text) + 1)
    table[0]=[[]]
    for i in range(len(text) + 1):
        ways=table[i]
        if ways is not None:
            for w in wordBank:
                if text[i:i + len(w)] == w :
                    new_combination=[ way +[w] for way in table[i]]
                    if table[i+len(w)] is not None:
                        new_ways= [way  for way in  table[i+len(w)]] + new_combination
                        table[i+ len(w)]=new_ways
                    else:
                        table[i+ len(w)]=new_combination
    return table[len(text)]
result = allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])
print(result)