'''
어떻게 풀어야 할지 몰라서 풀이 검색
막상 풀이를 보고나니 생각보다 안어려웠다

[ Point ]
1. lock을 2*M+N의 board로 확장 후, lock 배열을 가운데에 배치!
2. 방향을 90도로 돌려가면서, 모든 열쇠를 넣어 본다 (왼쪽으로 쭉이동... 아래로 이동...)
'''

#90도 회전
def rotation(rotationKey):
    return list(zip(*rotationKey[::-1]))

#열쇠 넣기
def attach(x,y,M,rotationKey,board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j]+=rotationKey[i][j]

#열쇠 빼기
def detach(x,y,M,rotationKey,board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j]-=rotationKey[i][j]

#모든 홈이 채워졌는지 체크
def check(board,M,N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j]!=1:
                return False
    return True

def solution(key, lock):
    M,N=len(key),len(lock)
    board=[[0]*(M*2+N) for _ in range(M*2+N)]
    #자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j]=lock[i][j]
    rotationKey=key
    #4방향 회전
    for _ in range(4):
        rotationKey=rotation(rotationKey)
        for x in range(1,M+N):
            for y in range(1,M+N):
                #열쇠 넣기
                attach(x,y,M,rotationKey,board)
                #모든 홈이 채워졌는지 check
                if check(board,M,N):
                    return True
                #열쇠 빼기
                detach(x,y,M,rotationKey,board)
    return False

#print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))