
# def countConstruct(text,wordBank):
#     if text=="":return 1

#     totalResult=0

#     for w in wordBank:
#         if text.startswith(w):
#             totalResult += countConstruct(text[len(w):],wordBank)
#     return totalResult


# result=countConstruct("purple",["purp","p","ur","le","purpl"])

# print("result ----",result)

def countConstructTabulation(text,wordBank):
    table=[0] * (len(text) + 1)
    table[0]=1
 
    for i in range(len(text)+ 1):
        current=table[i]
        if current !=0:
            for w in wordBank:
                if text[i:i+len(w)]==w and i+len(w) <=len(text):
                    table[i+len(w)] +=current
    return table[len(text)]




result=countConstructTabulation("purple",["purp","p","ur","le","purpl"])

print("result ----",result)