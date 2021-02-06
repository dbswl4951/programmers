import math

def lcm(x,y,g):
    return g*(x//g)*(y//g)

def solution(arr):
    if len(arr)==1: return arr[0]
    x,y=arr[0],arr[1]
    g=math.gcd(x,y)
    l=lcm(x,y,g)
    for i in range(2,len(arr)):
        g=math.gcd(l,arr[i])
        l=lcm(l,arr[i],g)
    return l

print(solution([2,6,8,14]))
print(solution([1,2,3]))