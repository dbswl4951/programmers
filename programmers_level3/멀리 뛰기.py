'''
규칙을 찾아내 점화식을 만드는 DP문제
피보나치 수열을 생각하면 된다 (dp[i]=dp[i-1]+dp[i-2])
'''
def solution(n):
    dp=[0]*(n+1)
    if n<3: return n
    dp[1],dp[2]=1,2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]%1234567