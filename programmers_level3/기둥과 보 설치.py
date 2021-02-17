'''
기둥, 보 설치가 가능 한 경우를 먼저 생각!
기둥, 보를 설치/제거 한후 설치된 모든 기둥과 보들이 주어진 조건에 맞게 설치되어 있는지 확인

기둥 설치가 가능한경우 :
1) 맨 밑에 있는 경우
2) 설치 아래 지점에 기둥이 있는 경우
3) 설치 왼쪽 지점에 보가 있는 경우
4) 설치 지점에 보가 있는 경우

보 설치가 가능한경우 :
1) 설치 아래 지점에 기둥이 있는 경우
2) 설치 아래 오른쪽 지점에 기둥이 있는 경우
3) 양 옆에 보가 있는 경우
'''

#설치가 가능한지 아닌지 체크 (설치 불가:True, 설치 가능:False)
def impossible(result):
    for x,y,a in result:
        #기둥
        if a==0:
            if y!=0 and (x,y-1,0) not in result and \
                    (x-1,y,1) not in result and (x,y,1) not in result:
                return True
        #보
        else:
            if (x,y-1,0) not in result and (x+1, y-1, 0) not in result and \
                    not ((x-1, y, 1) in result and (x+1, y, 1) in result):
                return True
    return False

def solution(n, build_frame):
    result=set()
    for x,y,a,b in build_frame:
        item=(x,y,a)
        #설치
        if b:
            #먼저 기둥, 보를 설치 한 후 조건에 맞게 설치 설치 됐는지 확인
            result.add(item)
            #조건에 맞게 설치 되지 않았다면 삭제
            if impossible(result):
                result.remove(item)
        #삭제
        elif item in result:
            #먼저 기둥, 보를 삭제 한 후 조건에 맞게 설치 됐는지 확인
            result.remove(item)
            #조건에 맞게 설치 되지 않았다면 다시 추가
            if impossible(result):
                result.add(item)
    result=map(list,result)
    return sorted(result,key=lambda x:(x[0],x[1],x[2]))

#print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
#print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
#print(solution(4,[[2,0,0,1],[3,0,0,1],[3,1,1,1],[4,1,0,1],[3,2,1,1],[2,1,1,1],[2,2,1,1],[2,1,1,0],[4,1,1,0]]))
#print(solution(6,[[1,1,1,1],[3,0,0,1],[5,0,0,1],[5,1,0,1],[6,1,1,1],[5,1,0,0],[2,0,0,1],[2,1,0,1],[2,2,0,1],[2,1,1,1],[1,2,1,1],[2,1,0,0]]))