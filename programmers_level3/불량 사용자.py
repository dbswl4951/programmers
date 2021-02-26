from itertools import permutations

#모든 경우의 수 확인
def isMatch(case,banned_id):
    for i in range(len(case)):
        if len(case[i])!=len(banned_id[i]):
            return False
        for j in range(len(case[i])):
            if banned_id[i][j]=='*': continue
            if case[i][j]!=banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    result=[]
    for case in permutations(user_id,len(banned_id)):
        if isMatch(case,banned_id):
            #중복 제거 위해 set() 사용
            case=set(case)
            if case not in result:
                result.append(case)
    return len(result)

#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))