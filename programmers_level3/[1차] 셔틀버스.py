def solution(n, t, m, timetable):
    #timetable을 분 단위로 변경
    timetable=[int(time[:2])*60 + int(time[3:5]) for time in timetable]
    timetable.sort()
    lastTime=(60*9)+(n-1)*t #셔틀 버스를 탈 수 있는 마지막 시간

    for i in range(n):
        #탈 수 있는 정원보다 승객의 수가 적다면, lastTime 리턴
        if len(timetable)<m:
            return '%02d:%02d'%(lastTime//60,lastTime%60)
        #마지막 버스
        if i==n-1:
            if timetable[0]<=lastTime:
                #탈 수 있는 가장 마지막 승객보다 1분 더 빨리
                lastTime=timetable[m-1]-1
            return '%02d:%02d'%(lastTime//60,lastTime%60)
        #마지막 버스 전까지, 셔틀 탄 승객들 timeTable에서 del
        for j in range(m-1,-1,-1):
            arrive=(60*9) +i*t  #버스 도착 시간
            if timetable[j]<=arrive:
                del timetable[j]

#print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
#print(solution(2,10,2,["09:10", "09:09", "08:00"]))
#print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"]))
#print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"]))
#print(solution(1,1,1,["23:59"]))
#print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
