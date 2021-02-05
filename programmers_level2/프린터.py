'''
전에 한 번 풀었던 문제인데도 다시 풀었을 때 잘 안풀렸다.
'''
def solution(priorities, location):
    #현재 대기 목록에 있는 문서의 index
    prop=[i for i in range(len(priorities))]
    output=[]
    while len(priorities)!=0:
        #우선 순위가 가장 높은 경우
        if priorities[0]==max(priorities):
            priorities.pop(0)
            output.append(prop.pop(0))
        else:
            #문서를 맨 뒤로 이동
            priorities.append(priorities.pop(0))
            prop.append(prop.pop(0))
    return output.index(location)+1

#print(solution([2, 1, 3, 2],2))
#print(solution([1, 1, 9, 1, 1, 1],0))