#올바른 괄호 문자열인지 체크
def checkStr(u):
    q=[]
    for uu in u:
        if uu == '(': q.append(uu)
        elif q:
            if uu==')':
                q.pop()
            else: return False
        else:
            if uu==')': return False
    return True

#균형잡힌 문자열 u,v로 분리
def sliceStr(w):
    leftCnt,rightCnt=0,0
    for i in range(len(w)):
        if w[i]=='(': leftCnt+=1
        else: rightCnt+=1
        if leftCnt==rightCnt:
            return w[:i+1],w[i+1:]

def solution(w):
    #(1) 과정
    if w=='': return w
    #(2) 과정
    u,v=sliceStr(w)
    #(3) 과정
    if checkStr(u):
        # (3-1) 과정
        return u+solution(v)
    #(4) 과정
    else:
        #(4-1),(4-2),(4-3) 과정
        temp='('+solution(v)+')'
        #(4-4) 과정
        tempU=u[1:len(u)-1]
        for t in tempU:
            if t==')':
                temp+='('
            else:
                temp+=')'
        #(4-5) 과정
        return temp

#print(solution("(()())()"))
#print(solution(")("))
#print(solution("()))((()"))