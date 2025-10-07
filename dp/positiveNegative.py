positiveWords="Good, Nice, Like, Mashallah, Barakallah, Tashakor, Khobis, Popular".lower().split(",")
negativeWords="Bad, Zesht, Lier, Manfi, Impossible, Mariz, Poor, Hunger".lower().split(",")
def findNegativePositive(tcs):
    for texts in tcs:
        countP=0
        countN=0
        for txt in texts:
            txt=txt.strip().lower()
            if any(word in txt for word in positiveWords):
                countP +=1
            elif any(word in txt for word in negativeWords):
                countN +=1
        print(f"Positive: {countP}, Negative: {countN}")

            


def main():

    T=int(input())
    tcs=[]
    for _ in range(T):
        commentN=int(input())
        texts=[input() for _ in range(commentN)]
        tcs.append(texts)
    findNegativePositive(tcs)


main()
    