'''
1. 문자열 슬라이드 사용해서 i개씩 분할
2. 분할 된 값을 now,next로 받음
3. 1) now==next
    ⇒ 앞,뒤 문자열이 일치하는 것이므로 num(숫자 중복이 얼마나 됐는지 나타내는 변수)을 1증가
    2) now≠next
    2-1)num==1이라면 중복되는 문자열 없으므로 그대로 temp 문자열에 더하기
    2-2) num≠1이라면 중복되는 문자열이 있다는 소리
    ⇒ temp에 num(중복된 횟수), 문자열 더하기
'''
def solution(s):
    result=[]
    for i in range(1,len(s)+1):
        j=0
        num=1
        temp=''
        while j<len(s):
            now,next=s[j:j+i],s[j+i:j+2*i]
            j+=i
            if now==next:
                num+=1
            else:
                if num!=1:
                    temp+=(str(num)+now)
                    num=1
                else:
                    temp+=now
        result.append(temp)
    rLen=int(1e9)
    for r in result:
        rLen=min(rLen,len(r))
    return rLen

#print(solution("aabbaccc"))
#print(solution("ababcdcdababcdcd"))
#print(solution("abcabcdede"))
#print(solution("abcabcabcabcdededededede"))
#print(solution("xababcdcdababcdcd"))