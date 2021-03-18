'''
N이 커서 이분탐색으로 생각하고 풀이 => 실패!
풀이 참고 후 문제 풀이
'''
def solution(n, stations, w):
    installRange=[]  #전기가 들어오지 않는 [start,end] 범위 저장
    start,end=1,0   #집의 시작점, 끝점 (시작은 1부터)
    result=0

    for station in stations:
        end=station-w-1
        #시작지점이 끝지점보다 더 크면 유효하지 않은 범위이므로 pass
        if start>end: pass
        else: installRange.append([start,end])
        #다음 시작 지점으로 이동
        start=station+w+1

    if start>n: pass
    #다음 시작지점이 n보다 작으면, start~n까지 범위 남아 있음
    else: installRange.append([start,n])

    for install in installRange:
        #2*w+1 : 포함 가능 한 전기 범위
        a=(install[1]-install[0]+1)//(2*w+1)
        b=(install[1]-install[0]+1)%(2*w+1)
        result+=a
        if b==0: pass
        else: result+=1
    return result

#print(solution(11,[4, 11],1))