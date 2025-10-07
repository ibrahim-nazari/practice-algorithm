


def calculate_change(test_cases):
    result=[]
    for test_case in test_cases:
        amount,coins=test_case
        sorted_coins=sorted(coins.items(),key=lambda x: -x[0])
        current_amount=amount
        bills=[]
        for denomination,count in sorted_coins:

            if current_amount==0:
                break
            bills_counts=min(current_amount//denomination,count)
            if bills_counts >0:
                bills_amount=bills_counts * denomination
                current_amount -=bills_amount
                bills.append((denomination,bills_counts))
            
        if current_amount==0:
            sorted_bills=sorted(bills, key=lambda x: -x[0])
            result.append(sorted_bills)
        else:
            result.append([("Impossible",None)])
    return result



def main():
    T=int(input())
    test_cases=[]
    for _ in range(T):
        amount=int(input())

        coins=list(input().split(","))
        coinsObject={}
        for coin in coins:
            denomination,count=map(int,coin.split(":"))
            coinsObject[denomination]=count
        test_cases.append((amount,coinsObject))
    result=calculate_change(test_cases)

    for i in range(len(result)):
        customer=result[i]
        for denomination,count in customer:
            if count==None:
                print(denomination)
            else:
                 print(str(denomination) +" " + str(count) )



if __name__ =="__main__":
 main()