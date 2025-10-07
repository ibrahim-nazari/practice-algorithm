
def prepare_bills(tcs):
    result=[]
    for amount,coins_data in tcs:
        sorted_data=sorted(coins_data,key=lambda x:(-x[0]))
        current_amount=amount
        bills_collections=[]
        for denomination,count in sorted_data:
            if current_amount==0:
                break
            bills=min(current_amount // denomination,count)
            if bills > 0:
                current_amount -= bills * denomination
                bills_collections.append((denomination,bills))
        if current_amount==0:

            result.append(bills_collections)
        else:
            result.append("Impossible")
    
    for i,rs in enumerate(result):
        print(f"Customer{i+1}:")
        if rs=="Impossible":
            print(rs)
            continue
        for d,count in rs:
            print(f"{d} {count}")




        

def main():
    tcs=[]
    T=int(input())
    for _ in range(T):
        amount=int(input())
        coins=input().split(",")
        coins_data=[tuple(map(int,coin.split(":"))) for coin in coins]

        tcs.append((amount,coins_data))
    prepare_bills(tcs)
if __name__ =="__main__":
    main()
