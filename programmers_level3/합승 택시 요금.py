'''
읽자마자 플로이드 와샬 알고리즘으로 풀어야겠다 생각했다.

각 노드의 최단거리는 구했지만, A와 B의 경로가 겹치는 부분을 어떻게 처리 할 지 몰라서 그 부분을 찾아봄
근데 찾아보고나니 겹치는 부분은 한 번만 수행해서 더해주면 되고, 거기에 k정점~A, k정점~B를 더해주면 되는 문제였다!
왜냐하면 플로이드 와샬은 모든 정점으로부터의 최소 거리를 구하는 것이 보장 되기 때문!!
=> 시작점~k + k~A + k~B

또한 계속 테스트 26번이 시간초과가 나서 찾아보다가
graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])를
if graph[i][j]>graph[i][k]+graph[k][j]의 조건문으로 바꿔줬더니 통과가 됐다..
'''
INF = int(1e9)

def floyd(n,graph):
    #k:거쳐 갈 노드 번호
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j]>graph[i][k]+graph[k][j]:
                    graph[i][j]=graph[i][k]+graph[k][j]
    return graph

def solution(n, s, a, b, fares):
    graph=[[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j]=0
    for start,end,dist in fares:
        graph[start][end]=dist
        graph[end][start]=dist
    graph=floyd(n,graph)
    result=INF
    for i in range(1, n + 1):
        result = min(result, graph[s][i] + graph[i][a] + graph[i][b])
    return result

#print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
#print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
