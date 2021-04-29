'''
[ POINT ]
1) 첫번째 집을 턴 경우 => 마지막 집 못 털음
2) 첫번째 집을 털지 않은 경우 => 마지막 집 털 수 있음
두 개의 경우로 나눠서 생각해야 함
'''

def solution(money):
    # 첫번째 집 턴 경우
    dp=[0]*len(money)
    dp[0],dp[1]=money[0],money[0]
    # 범위에서 마지막 집 제외
    for i in range(2,len(money)-1):
        dp[i]=max(dp[i-2]+money[i],dp[i-1])
    result=max(dp)

    # 첫번째 집 털지 않은 경우
    dp = [0] * len(money)
    dp[1]=money[1]
    # 마지막 집 털 수 있음 (범위에 포함)
    for i in range(2,len(money)):
        dp[i]=max(dp[i-2]+money[i],dp[i-1])
    result=max(result,max(dp))
    return result

#print(solution([1,2,3,1]))
#print(solution([7,1,1,6,3]))