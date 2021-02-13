'''
처음에 Trie 알고리즘인가? 생각해서 트라이 알고리즘을 찾아보고 비슷하게 구현하려다가 복잡해서 답 찾아봄
단순 조합 문제였다..
'''
from itertools import combinations
from collections import Counter

def solution(orders, course):
    result=[]
    for c in course:
        temp=[]
        for order in orders:
            combi = combinations(sorted(order),c)
            temp+=combi
        #Counter : 컨테이너에 동일한 값의 자료가 몇개인지 리턴 (ex:{'a':3, 'b':1}..)
        counter=Counter(temp)
        #같은 조합이 2번 이상 나타난다면 메뉴 조합 고려
        if len(counter)!=0 and max(counter.values())!=1:
            #메뉴 조합 중(for i in counter)
            #가장 많이 주문 된 조합을(if counter[i]==max(counter.values()))
            #문자열로 result에 추가 (''.join(i))
            result+=[''.join(i) for i in counter if counter[i]==max(counter.values())]
    return sorted(result)


#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))