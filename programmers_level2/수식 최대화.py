from itertools import permutations
import re   #re : 파이썬 정규 표현식 지원

def solution(expression):
    #re.findall('\D') : 숫자가 아닌것을 모두 찾음
    expressions=set(re.findall('\D',expression))
    result=[]
    for case in permutations(expressions):
        #re.compile(검색할문자열) : 정규식 객체 리턴
        temp=re.compile("(\D)").split(''+expression)
        for c in case:
            while c in temp:
                #연산자 위치 찾음
                idx=temp.index(c)
                temp=temp[:idx-1]+[str(eval(''.join(temp[idx-1:idx+2])))]+temp[idx+2:]
        result.append(abs(int(temp[0])))
    return max(result)

#print(solution("100-200*300-500+20"))
#print(solution("50*6-3*2"))