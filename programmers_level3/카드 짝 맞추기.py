from collections import deque
import copy

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(board, r, c):
    answer = 0
    b = ""
    for i in range(4):
        for j in range(4):
            b+=str(board[i][j])
    q=deque()
    print(b)
    cnt=0
    enter=-1
    q.append((r,c,b,cnt,enter))
    s=set()

    while q:
        x,y,b,cnt,enter=q.popleft()
        pos=4*x+y

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))
#print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1))