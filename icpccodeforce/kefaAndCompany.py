n,d=map(int,input().split())
moneyFriendShip=[tuple(map(int,input().split())) for _ in range(n)]
moneyFriendShip.sort(key=lambda x: x[0])
l=0
cur_sum=0
max_sum=0
for r in range(n):
    p1=moneyFriendShip[l]
    p2=moneyFriendShip[r]
    cur_sum +=p2[1]
    while p2[0] - moneyFriendShip[l][0] >=d:
        cur_sum -=moneyFriendShip[l][1]
        l+=1
    max_sum=max(max_sum,cur_sum)
print(max_sum)