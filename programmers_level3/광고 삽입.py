'''
DP + Memoization 문제

1. 모든 시간을 '초'단위로 변경
2. 모든 로그의 시작,끝지점을 '초'단위로 변경 후 DP 테이블에 시작,끝 지점에 시청자 수 반영
3. DP에 구간 별 시청자 수 기록 (시작+1~끝-1까지 다 표시 해줌)
4. 모든 구간 시청자 누적 기록
5. 누적된 시청자수를 바탕으로 시청자 수가 가장 많은 구간 탐색

다른 사람 풀이 참고
'''

#모든 시간을 초 단위로 변경
def convertToSeconds(time):
    h,m,s=time.split(':')
    return int(h)*3600 + int(m)*60 + int(s)

def solution(play_time, adv_time, logs):
    # [1번 과정] : 시간을 초단위로 변경
    convertToSeconds(play_time)
    convertToSeconds(adv_time)
    timeDP = [0 for i in range(play_time+1)]    #시간별 시청자 수를 기록하는 dp 테이블
    # [2번 과정] : log를 초단위로 변경, 시청 시간의 처음과 끝을 DP 리스트에 표시
    for l in logs:
        start,end=l.split('-')
        start,end=convertToSeconds(start),convertToSeconds(end)
        #timeDP[i] : i시각에 시청중인 사람의 수
        timeDP[start]+=1
        timeDP[end]-=1
    # [3번 과정] : 모든 구간에 시청자 수 기록
    for i in range(1,len(timeDP)+1):
        timeDP[i]=timeDP[i]+timeDP[i-1]
    # [4번 과정] : 모든 구간 시청자 누적 기록
    for i in range(1, len(timeDP) + 1):
        timeDP[i] = timeDP[i] + timeDP[i - 1]
    mostView=0
    maxTime=0
    # [5번 과정] : 누적된 시청자 수를 기반으로 (i시간의 누적 시청자 수 - (i-adv_time)의 누적 시청자 수)
    #for i in range(adv_time-1,play_time):



print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))