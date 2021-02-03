'''
    [1]                [1]
   [2][9]              [2][9]
 [3][10][8]    ->      [3][10][8]
[4][5][6][7]           [4][5][6][7]

방향은 down, right, up 3가지가 반복된다.
i % 3 == 0이면 down
i % 3 == 1이면 right
i % 3 == 2이면 up
'''

def solution(n):
    triangle=[[0]*n for _ in range(n)]
    x,y=-1,0
    num=1
    result=[]
    for i in range(n):
        for j in range(i,n):
            #down
            if i%3==0:
                x+=1
            #right
            elif i%3==1:
                y+=1
            #up
            else:
                x-=1
                y-=1
            triangle[x][y]=num
            num+=1
    for i in range(n):
        for j in range(n):
            if triangle[i][j]!=0:
                result.append(triangle[i][j])
    return result

#solution(6)