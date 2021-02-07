'''
문제를 이해하기 어려웠고, 답안을 보고 나니 풀이 자체는 간단하게 느껴졌지만 재귀 함수 구현이 어려웠다.
'''
#문자열 w를 u,v로 분리
def slice(w):
    open,close=0,0
    for i in range(len(w)):
        if w[i]=='(': open+=1
        else: close+=1
        if open==close:
            return w[:i+1],w[i+1:]

#올바른 괄호 문자열인지 체크
def check(u):
    q=[]
    for i in u:
        if i=='(': q.append(i)
        elif q: q.pop()
    if q: return False
    return True

def solution(w):
    #과정 1
    if not w: return w
    #과정 2
    u,v=slice(w)
    #과정 3 (어려웠던 재귀 부분!)
    if check(u):
        return u+solution(v)
    #과정 4 (이 과정도 마찬가지로 '재귀적으로 수행한 결과 문자열'을 이어 붙여야 한다!)
    s='('+solution(v)+')'
    uu=u[1:len(u)-1]
    for i in uu:
        if i=='(': s+=')'
        else: s+='('
    return s

#print(solution("(()())()"))
#print(solution(")("))
#print(solution("()))((()"))