def solution(land):
    dp=[[0]*4 for _ in range(len(land))]
    for i in range(4):
        dp[0][i]=land[0][i]
    for i in range(1,len(land)):
        dp[i][0]=max(dp[i-1][1],dp[i-1][2],dp[i-1][3])+land[i][0]
        dp[i][1]=max(dp[i-1][0],dp[i-1][2],dp[i-1][3]) + land[i][1]
        dp[i][2]=max(dp[i-1][0],dp[i-1][1],dp[i-1][3]) + land[i][2]
        dp[i][3]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2]) + land[i][3]
    return max(dp[-1])

#print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))