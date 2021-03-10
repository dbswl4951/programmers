'''
현재 위치%2==0 이면 건전지 사용X
'''
def solution(n):
    result=0
    while n>0:
        #divmod(): 몫, 나머지 구함
        n,m=divmod(n,2)
        #+ 점프하는데 쓰는 비용(m)
        result+=m
    return result

#DP 사용 => 시간 초과
'''
def solution(n):
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        if i%2==0:
            dp[i]=dp[i//2]
        else:
            dp[i]=dp[i-1]+1
    return dp[-1]
'''

#print(solution(5))
#print(solution(6))
#print(solution(5000))