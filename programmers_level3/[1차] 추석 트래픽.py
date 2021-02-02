'''
제한을 1시간 잡고 풀었는데 datetime을 사용 해 보지 않아서 찾느라
각 로그의 시작시간, 끝시간을 구하는 것 까지 밖에 못했다.
해설 찾아 봄
'''
#timedelta : 시간을 더하거나 빼기 위해 사용
from datetime import datetime, timedelta

def countLog(t,times):
    count=0
    for idx,time in enumerate(times):
        if time[1]>=t and time[0]<t+timedelta(milliseconds=1000):
            count+=1
    return count

def solution(lines):
    times=[]
    for line in lines:
        day,time,delaySec=line.split(' ')
        #요청 처리 끝나는 시간을 datetime으로 변경
        end=datetime.strptime(day+' '+time,'%Y-%m-%d %H:%M:%S.%f')
        #delaySec을 milli second로 변경
        delayMilliSec=int(float(delaySec[:-1])*1000)
        start=end-timedelta(milliseconds=delayMilliSec)+timedelta(milliseconds=1)
        times.append([start,end])
        #print(start,"///",end)
    count=0
    for time in times:
        #요청량이 변하는 순간은 각 로그의 시작과 끝 부분이므로, 요청 시작/끝 부분의 count 수 검사
        count=max(count,countLog(time[0],times),countLog(time[1],times))
    #print(count)
    return count


'''
solution(['2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
])
'''