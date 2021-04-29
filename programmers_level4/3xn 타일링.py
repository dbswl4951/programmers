'''
생각해내기 어려운 점화식이었다
'''
def solution(n):
    dp=[0,3,11]
    # 짝수만 고려
    idx=n//2
    if n%2!=0: return 0
    if idx<3: return dp[idx]

    for i in range(3,idx+1):
        dp.append(3*dp[i-1]+sum(dp[1:i-1])*2+2)
    return dp[idx]%1000000007
