from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(maps):
    nLen,mLen=len(maps),len(maps[0])
    print(nLen,mLen)
    q=deque()
    q.append([0,0])
    visited=[[0]*mLen for _ in range(nLen)]
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        if x==nLen-1 and y==mLen-1: break
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<nLen and 0<=ny<mLen and maps[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                q.append([nx,ny])
    if visited[nLen-1][mLen-1]==0:
        return -1
    else:
        return visited[nLen-1][mLen-1]

def solution(maps):
    return bfs(maps)

#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
#print(solution([[1,0,0,1],[1,1,0,1],[1,1,1,1],[1,0,1,1],[1,0,0,1]]))