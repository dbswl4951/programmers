from itertools import permutations

def solution(n, weak, dist):
    l=len(weak)
    cand=[]
    #선형으로 만들기 위해 배열 덧붙여 줌
    weakList=weak+[w+n for w in weak]
    #i:index, start:시작 지점 위치
    for i,start in enumerate(weak):
        #friends : (3, 5, 7), (3, 7, 5)...
        for friends in permutations(dist):
            count=1         #count: 투입 된 친구 수
            position=start  #position : 현재 위치
            #친구 한 명씩 배치하면서 끝까지 도달 할 수 있는지 확인
            for friend in friends:
                position += friend  #친구가 이동 할 수 있는 거리만큼 이동 후, 현재 위치 갱신
                #끝까지 도달하지 못하면
                if position<weakList[i+l-1]:
                    count+=1    #친구 한 명 더 투입
                    #현재 위치 (position)보다 멀리 있는 취약 지점 중, 가장 가까운 위치로 설정
                    position=[w for w in weakList[i+1:i+l] if w>position][0]
                #끝까지 도달
                else:
                    cand.append(count)
                    break
    return min(cand) if cand else -1

#print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
#print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))