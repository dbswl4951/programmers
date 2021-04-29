def floyd(n,dist):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    return dist

def solution(n, s, a, b, fares):
    dist=[[int(1e9)]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j: dist[i][j]=0
    for x,y,z in fares:
        dist[x][y]=z
        dist[y][x]=z
    dist=floyd(n,dist)

    result=int(1e9)
    for i in range(1,n+1):
        result=min(result,dist[s][i]+dist[i][a]+dist[i][b])
    return result

#print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
#print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
#print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))