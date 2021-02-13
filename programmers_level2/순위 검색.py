'''
for문을 이용해 문자열을 탐색하면 정확도 100퍼는 받을 수 있지만, **효율성 테스트** 탈락!

<lower bownd 알고리즘 사용>
'-'를 포함한 조건상의 모든 경우에 대해 데이터를 저장하고,
이진탐색을 통해 주어진 점수값보다 높은 점수를 가진 데이터의 갯수를 얻어냄

1. info에 대해 '-'를 포함한 모든 경우의 수 생성 후, 경우의 수를 키값으로 하는 딕셔너리에 score저장
3. 주어진 query에 대해 딕셔너리를 확인 후,
 값이 있을 경우 lower bownd를 통해 query의 점수보다 크거나 같은 최대값 찾음
'''
from itertools import combinations
from collections import defaultdict

def solution(info, queries):
    answer=[]
    #defaultdict(): 호출과 동시에 미리 지정한 기본값이 할당되도록 선언
    dict=defaultdict(list)
    for info in info:
        info=info.split()
        #점수를 제외한 info 정보를 key값으로, 점수를 value값으로 딕셔너리 생성
        infoKey=info[:-1]
        infoVal=int(info[-1])
        #[1번 과정] : '-'를 포함한 모든 경우의 수 생성 후, 경우의 수를 키값으로 하는 딕셔너리 생성
        for i in range(5):
            for c in combinations(infoKey,i):
                tempKey=''.join(c)
                #가능한 info 조합을 key, 점수를 value로 딕셔너리 저장
                dict[tempKey].append(infoVal)
    #value값을 오름차순으로 정렬
    for key in dict.keys():
        dict[key].sort()
    #queries를 조건,점수로 나눔
    for query in queries:
        query=query.split(' ')
        queryScore = int(query[-1])
        query=query[:-1]
        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tempQuery=''.join(query)

        #[2번 과정] : lower bound 알고리즘 사용해 score보다 큰 점수 개수 구하기
        if tempQuery in dict:
            scores=dict[tempQuery]
            if len(scores)>0:
                #lower bound는 배열크기 만큼 리턴되어야 하기 때문에 end = array.length -1 이 아니고 end = array.length로 지정 해야 함
                start,end=0,len(scores)
                while start<end:
                    mid=(start+end)//2
                    if scores[mid]>=queryScore:
                        end=mid
                    else:
                        start=mid+1
                #start의 값이 queryScore 점수 이상인 값이 처음 나오는 인덱스
                #전체 개수 - (start 전까지의 요소 개수) = start~끝까지의 개수
                answer.append(len(scores)-start)
        else:
            answer.append(0)
    return answer

#print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))