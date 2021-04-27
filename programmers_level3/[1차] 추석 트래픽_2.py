# 1초에 몇 개나 처리 됐는지 계산
def getThroughput(stanTime,timeList):
    cnt = 0
    for time in timeList:
        if time[0]<stanTime+1 and time[1]>=stanTime:
            cnt+=1
    return cnt

def solution(lines):
    timeList=[]
    for l in lines:
        date,time,duration=l.split(' ')
        t=list(time.split(':'))
        endSec=int(t[0])*3600+int(t[1])*60+float(t[2])
        durSec=float(duration[:len(duration)-1])
        startSec=round(endSec-durSec+0.001,3)
        timeList.append([startSec,endSec])
    timeList.sort()

    result=0
    for time in timeList:
        # 요청량이 변하는 구간은 로그의 시작과 끝
        result=max(result,getThroughput(time[0],timeList),getThroughput(time[1],timeList))
    return result


'''
print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
'''