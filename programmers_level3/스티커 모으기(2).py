'''
첫 번째 스티커를 떼는지, 두 번째 스티커를 떼는지에 따라 인덱스 범위를 다르게 줘야 함
'''

def solution(sticker):
    if len(sticker)==1: return sticker[0]
    dp1=[0]*len(sticker)
    dp2 =[0] * len(sticker)
    dp1[0],dp1[1],dp2[0],dp2[1]=sticker[0],sticker[0],0,sticker[1]

    # 첫번째 스티커를 떼는 경우
    for i in range(2,len(sticker)-1):
        dp1[i]=max(dp1[i-2]+sticker[i],dp1[i-1])

    # 두번째 스티커를 떼는 경우
    for i in range(2,len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    return max(dp1[-2],dp2[-1])

#print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
#print(solution([1, 3, 2, 5, 4]))
#print(solution([1,8,1,2,6,1,1,6]))
#print(solution([1,3]))