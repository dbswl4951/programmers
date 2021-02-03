'''
양방향 + bfs 사용

union-find로 풀었으면 더 쉽게 풀었을 것 같다.
'''
from collections import deque

def bfs(i,graph,visited):
    q=deque()
    q.append(i)
    visited[i]=1
    while q:
        now=q.popleft()
        visited[now]=1
        for i in graph[now]:
            if visited[i]==0:
                q.append(i)

def solution(n, computers):
    graph=[[] for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i!=j and j not in graph[i] and computers[i][j]==1:
                graph[i].append(j)
                graph[j].append(i)
    visited=[0]*n
    result=0
    for i in range(n):
        if visited[i]==0:
            bfs(i,graph,visited)
            result+=1
    return result

#print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
#print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
#print(solution(6,[[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]))
#print(solution(4,[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))
#print(solution(6,[[1,0,0,0,0,0],[0,1,0,1,0,1],[0,0,1,0,1,0],[0,1,0,1,0,1],[0,0,1,0,1,0],[0,0,0,1,0,1]]))