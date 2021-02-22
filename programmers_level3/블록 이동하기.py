from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque() #이동해야 할 좌표
visited = []  #방문했던 좌표 저장

def bfs(robot,board):
    bLen=len(board)-1
    q.append(robot)
    visited.append(robot)
    cnt=0
    while q:
        qLen=len(q)
        while qLen:
            cur=q.popleft()
            if cur==[[bLen,bLen-1],[bLen,bLen]] or cur==[[bLen-1,bLen],[bLen,bLen]]:
                return cnt
            #로봇 상하좌우 이동
            for i in range(4):
                temp=[]     #회전 전 이동 좌표 임시 저장 변수
                flag=0      #범위 내에 있는지 체크하는 변수
                #j==0:로봇 머리 이동, j==1:로봇 꼬리 이동
                for j in range(2):
                    nx=cur[j][0]+dx[i]
                    ny=cur[j][1]+dy[i]
                    if 1<=nx<=bLen and 1<=ny<=bLen and board[nx][ny]==0:
                        temp.append([nx,ny])
                    else:
                        flag=1
                        break
                #회전 할 수 있는지 체크
                if not flag:
                    if cur[0][0]==cur[1][0]:    #로봇이 가로 방향이고
                        if i==0 or i==1:        #위,아래로 이동 가능하면 회전 가능
                            turn(cur,i,0)
                    elif cur[0][1]==cur[1][1]:  #로봇이 세로 방향이고
                        if i==2 or i==3:        #좌,우로 이동 가능하면 회전 가능
                            turn(cur,i,1)
                    temp.sort()
                    #회전 전 임시 좌표를 아직 방문 안했으면 방문
                    if temp not in visited:
                        q.append(temp)
                        visited.append(temp)
            qLen-=1
        cnt+=1

#90도 회전
def turn(cur,i,s):
    #가로->세로
    if s==0:
        #j==0:로봇 머리 고정하고 회전, j==1:로봇 꼬리 고정하고 회전
        for j in range(2):
            nx,ny=cur[j], [cur[j][0]+dx[i],cur[j][1]]
            temp=[nx,ny]
            #회전 시킨 로봇 위치가 처음 방문하는 것이면 큐에 삽입
            if temp not in visited:
                q.append(temp)
                visited.append(temp)
    #세로->가로
    if s==1:
        #j==0:로봇 머리 고정하고 회전, j==1:로봇 꼬리 고정하고 회전
        for j in range(2):
            nx,ny=[cur[j][0],cur[j][1]+dy[i]], cur[j]
            temp=[nx,ny]
            temp.sort()
            # 회전 시킨 로봇 위치가 처음 방문하는 것이면 큐에 삽입
            if temp not in visited:
                q.append(temp)
                visited.append(temp)

def solution(board):
    board=[[0]*(len(board)+1)]+board
    for i in range(1,len(board)):
        board[i]=[0]+board[i]
    robot=[[1,1],[1,2]]
    return (bfs(robot,board))

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))