from itertools import combinations

def solution(relation):
    row=len(relation)
    col=len(relation[0])
    case=[]
    #전체 조합 구하기
    for i in range(1,col+1):
        case.extend(combinations(range(col),i))
    #유일성 : 유일하게 식별 되야 함
    unique=[]
    for c in case:
        #인덱스 번호 -> 요소 값으로 변경 후 temp에 tuple 형태로 저장
        temp=[tuple([re[i] for i in c]) for re in relation]
        #print("temp:",temp)
        if len(set(temp))==row:
            unique.append(c)
    #print("unique:", unique)
    result=set(unique)
    #최소성 : 최소한의 요소로 유일성 만족 시켜야 함
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            #intersection() : 튜플 사이의 교집합 구함 (==&)
            if len(unique[i])==len(set(unique[i]).intersection(set(unique[j]))):
                #print(set(unique[i]),set(unique[j]))
                #discard(): 삭제 할려는 요소가 없어도 정상 종료 (remove()는 KeyError 발생)
                result.discard(unique[j])
    return len(result)

#print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))