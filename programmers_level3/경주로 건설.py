from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(board):
    bLen=len(board)
    visited=[[0 for _ in range(bLen)] for _ in range(bLen)]
    q=deque()
    q.append([0,0,0,0]) #[x,y,방향,가격]
    while q:
        x,y,dir,cost=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<bLen and 0<=ny<bLen and board[nx][ny]==0 and not(nx==0 and ny==0):
                if x==0 and y==0:
                    newCost=100
                elif dir==i:
                    newCost=cost+100
                else:
                    newCost=cost+600
                if visited[nx][ny]==0 or visited[nx][ny]>=newCost:
                    visited[nx][ny]=newCost
                    q.append([nx,ny,i,newCost])
    return visited[-1][-1]

def solution(board):
    return bfs(board)

#print(solution([[0,0,0],[0,0,0],[0,0,0]]))
#print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
#print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
#print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))