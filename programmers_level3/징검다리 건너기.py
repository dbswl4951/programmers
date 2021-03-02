'''
이분 탐색 사용

탐색 대상 : 친구들 수
돌의 높이 - 건넌 친구 수 <0 : cnt+1
        >=0 (연속이 아닐 경우) : cnt=0
=> O(nlogm)
'''
#연속으로 0이 k이상 나타나는지 확인
def check(mid,stones,k):
    cnt=0
    for s in stones:
        if s-mid<=0: cnt+=1
        else: cnt=0
        if cnt>=k: return True
    return False

def solution(stones, k):
    start,end=1,200000000
    while start<=end:
        mid=(start+end)//2
        if check(mid,stones,k):
            end=mid-1
        else:
            start=mid+1
    return start

#print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))