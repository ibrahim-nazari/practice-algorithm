import math

def circumcircle_area(n, a):
    R = a / (2 * math.sin(math.pi / n))
    return math.pi * R * R

# example
n,s=map(int,input().split())
print(circumcircle_area(n, s))  # prints 3.141592653589793
