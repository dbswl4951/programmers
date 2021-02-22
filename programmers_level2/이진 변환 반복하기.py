def solution(s):
    result=[0,0]
    while s!='1':
        result[0]+=1
        result[1]+=s.count('0')
        s=s.replace('0','')
        sLen=len(s)
        s=bin(sLen)[2:]
    return result

#print(solution("110010101001"))
#print(solution("01110"))
#print(solution("1111111"))