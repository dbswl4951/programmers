#x,y 범위 체크
def checkRange(x,y):
    if -5<=x<=5 and -5<=y<=5:
        return 1
    return 0

def solution(dirs):
    x,y=0,0
    s=set()
    for dir in dirs:
        #위쪽 이동
        if dir=='U':
            if checkRange(x,y+1):
                y += 1
                if ((x,y-1),(x,y)) not in s and ((x,y),(x,y-1)) not in s:
                    s.add(((x, y-1),(x,y)))
        #아래쪽 이동
        elif dir=='D':
            if checkRange(x,y-1):
                y -= 1
                if ((x,y),(x,y+1)) not in s and ((x,y+1),(x,y)) not in s:
                    s.add(((x, y+1),(x,y)))
        #왼쪽 이동
        elif dir=='L':
            if checkRange(x-1,y):
                x -= 1
                if ((x+1,y),(x,y)) not in s and ((x,y),(x+1,y)) not in s:
                    s.add(((x+1, y),(x,y)))
        #오른쪽 이동
        else:
            if checkRange(x+1,y):
                x += 1
                if ((x-1,y),(x,y)) not in s and ((x,y),(x-1,y)) not in s:
                    s.add(((x-1, y),(x,y)))
    return len(s)

#print(solution('ULURRDLLU'))
#print(solution('LULLLLLLU'))
#print(solution('RRULDRLD'))