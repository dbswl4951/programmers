'''
k가 극단적으로 크기 때문에, 리스트 생성보다는 딕셔너리러 생성
rommDict.get()사용보다, defaultdict() 사용이 더 시간적인 면에서 좋다!
roomDic은 key방을 원하는 사람이 있다면, value방에 배치된다는 의미

(1) 현재 노드 -> 다음 노드 탐색 후,
(2) 현재 노드 = 다음 노드
빈 방이 발견 될 때까지 (1), (2) 반복
'''
from collections import defaultdict

def solution(k, room_number):
    result=[]
    roomDict= defaultdict(int)

    for number in room_number:
        num=roomDict[number]

        # 방이 차있는 경우
        if num:
            # 방문 한 노드들 저장 => 나중에 갱신 하기 위해서
            passRomm=[number]
            while True:
                now=num
                # 현재 노드 (now)로 다음 노드 얻기
                num=roomDict[now]
                # 다음 방이 비어있는 경우
                if not num:
                    result.append(now)
                    roomDict[now]=now+1
                    # 이전에 거쳤던 노드들 갱신
                    for room in passRomm:
                        roomDict[room]=now+1
                    break
                passRomm.append(num)

        # 방이 비어있어서, 원하는 방을 선택 할 수 있는 경우
        else:
            result.append(number)
            roomDict[number]=number+1
    return result

#print(solution(10,[1,3,4,1,3,1]))
#print(solution(7,[1,3,3,3,4]))