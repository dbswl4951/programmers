def solution(n):
    if n==1: return 1
    a,b=n,n-1
    result=0
    while a>-1 and b>-1:
        s=((a*(a+1))//2)-((b*(b+1))//2)
        if s==n:
            result+=1
            b-=1
        elif s<n: b-=1
        else: a-=1
    return result
#print(solution(15))