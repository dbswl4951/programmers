def solution(m, n, board):
    newBoard=[]
    for b in board:
        newBoard.append(list(b.strip()))
    result=0

    while True:
        upIdx = [-1] * n
        delete = set()
        # 블럭 삭제
        for i in range(m-1):
            for j in range(n-1):
                if newBoard[i][j] and newBoard[i][j]==newBoard[i][j+1] and newBoard[i][j]==newBoard[i+1][j] and newBoard[i][j]==newBoard[i+1][j+1]:
                    delete.add((i,j))
                    delete.add((i+1,j))
                    delete.add((i,j+1))
                    delete.add((i+1,j+1))
                    if upIdx[j+1]<i+1:
                        upIdx[j]=i+1
                        upIdx[j+1]=i+1
        if not delete: break
        for x,y in delete:
            newBoard[x][y]=0
            result+=1

        # 블럭 내리기
        for j in range(n):
            if upIdx[j]>1:
                for i in range(upIdx[j]-2,-1,-1):
                    if newBoard[i][j]!=0:
                        newBoard[upIdx[j]][j]=newBoard[i][j]
                        newBoard[i][j]=0
                        upIdx[j]-=1
    return result

#print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
#print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
#print(solution(5,6,['AAAAAA','BBAATB','BBAATB','JJJTAA','JJJTAA']))