


# def canConstruct(text,wordsArray,memo={}):
#     if text in memo: return memo[text]

#     if text =="" :return True

#     for w in wordsArray:
#         if w== text[0:len(w)]:
#             remainderText=text[len(w):]
#             if canConstruct(remainderText,wordsArray) ==True:
#                 memo[text]=True
#                 return True
    
#     memo[text]=False
#     return False



# result=canConstruct("abcdcdab",["ab","abc","cd","def","abcd"])

# print("result ----",result)

def canCunstruct(text,wordBank):

    table=[False] * (len(text) + 1)
    table[0]=True

    for i in range(len(text) + 1):
        if table[i]==True:
            for w in wordBank:
                if text[i:i+len(w)]==w and i+len(w) <= len(text):
                    table[i+len(w)]=True

    return table[len(text)]




result = canCunstruct("abcdef",["ab","abc","cd","def","abcd"])

print("result ----",result)
