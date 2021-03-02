'''
투포인터 사용

모든 보석을 포함 할 때까지 end 증가 후, start를 1씩 증가시킴
=> 알고리즘, 접근 방식은 맞았으나 반례 발생해 풀이 참고

[ 다른 사람 풀이 보고 알게 된 점 ]
set()대신 딕셔너리 사용으로 start~end 구간이 모든 보석을 포함하는지 검사
=> 딕셔너리를 사용해야지 중복 된 보석의 수 처리도 가능하다!
'''
def solution(gems):
    gLen,sLen=len(gems),len(set(gems))
    start,end=0,0
    sDict={gems[0]:1}
    result=[0,gLen-1]
    while start<gLen and end<gLen:
        #모든 보석이 포함 됐을 때 시작점(start) 이동
        if len(sDict)==sLen:
            #더 최솟거리로 result 배열 갱신
            if result[1]-result[0]>end-start:
                result=[start,end]
            #보석 수가 1이면 딕셔너리에서 삭제, 2이상이면 보석수 -1
            if sDict[gems[start]]==1:
                del sDict[gems[start]]
            else:
                sDict[gems[start]]-=1
            start+=1
        #보석이 아직 다 포함 안됐을 때 끝점(end) 이동
        else:
            end+=1
            #맨 끝에 도달하면 break
            if end==gLen: break
            #새로운 보석이면 1로 초기화 후, 딕셔너리에 추가
            if not sDict.get(gems[end]):
                sDict[gems[end]]=1
            #이미 있는 보석인 경우 +1
            else:
                sDict[gems[end]]+=1
    return [result[0]+1,result[1]+1]

#print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
#print(solution(["AA", "AB", "AC", "AA", "AC"]))
#print(solution(["XYZ", "XYZ", "XYZ"]))
#print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))