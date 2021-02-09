'''
1. 처음과 끝의 값은 끝까지 남길 수 있다.
2. 가운데 값은 left = 첫 번째 값, right = 마지막값으로 출발하여 자기보다 작은수를 남길 수 있다.
 작은수를 발견할때마다 자기자신을 갱신하면서 끝까지 간다.

어떻게 풀어야 할지 감이 안잡혀서 다른 사람 풀이를 봤다.
'''

def solution(a):
    answer=2
    if 0<=len(a)<=2: return len(a)
    left,right=a[0],a[-1]
    for i in range(1,len(a)-1):
        if left>a[i]:
            answer+=1
            left=a[i]
        if right>a[-1-i]:
            answer+=1
            right=a[-1-i]
    return answer if left!=right else answer-1

print(solution([7,8,0,2,-5,-3]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))