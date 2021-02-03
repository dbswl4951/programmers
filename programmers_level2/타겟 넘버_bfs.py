from collections import deque

def solution(numbers, target):
    q=deque()
    q.append([0,0])
    result=0
    while q:
        val,idx=q.popleft()
        #numbers의 모든 수를 다 사용했을 때
        if idx==len(numbers):
            if val==target:
                result+=1
        #numbers의 모든 수를 아직 다 사용 하지 않았을 때, 연산 후 큐에 삽입
        else:
            q.append([val+numbers[idx],idx+1])
            q.append([val-numbers[idx],idx+1])
    return result

#print(solution([1,1,1,1,1],3))