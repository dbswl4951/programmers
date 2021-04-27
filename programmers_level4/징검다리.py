def solution(distance, rocks, n):
    if len(rocks)==1: return 0
    rocks.sort()
    start,end=0,rocks[-1]-rocks[0]

    result=0
    while start<=end:
        mid=(start+end)//2
        cnt=0   # 건너 뛴 횟수
        before=0    # 건너 뛰기 전 수
        minVal=int(1e9)
        for rock in rocks:
            if rock-before<mid: cnt+=1
            else:
                # 거리의 최솟값 구하기
                minVal=min(minVal,rock-before)
                before=rock

        if cnt>n:
            end=mid-1
        if cnt<=n:
            # 조건을 만족하는 거리의 최솟값 중 가장 큰 값 구하기
            result=max(result,minVal)
            start=mid+1
    return result


#print(solution(25,[2, 14, 11, 21, 17],2))
#print(solution(30,[4,6,7,9,16,18,21],3))