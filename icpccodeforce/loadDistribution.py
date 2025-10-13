# aidar 1- n
# vikar from n -1
# x fixed number
# output
# aidar , vikar, x read
# input
# first line number of question
# second line x is reading
#  nex line direction
# https://codeforces.com/gym/106110/problem/A
import math

n=int(input())
xstart=int(input())
dir=input().strip()
first=second=third=0
if dir=="L":
    third=n-xstart
    first=second= math.ceil(xstart/2)
else:
    first =xstart -1
    third=second= math.ceil((n-xstart+1)/2)
print(first,second,third)
