def solution(msg):
    # 1번
    dic={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,"G":7,'H':8,'I':9,'J':10,
         'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
         'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

    result=[]
    while len(msg)>0:
        # 2번
        w=''
        for m in msg:
            if w+m in dic.keys(): w+=m
            else: break

        # 3번
        result.append(dic[w])
        msg=msg[len(w):]

        # 4번
        if msg!='':
            if w+msg[0] not in dic.keys():
                dic[w+msg[0]]=len(dic)+1
        elif w not in dic.keys():
            dic[w]=len(dic)+1

    return result

#print(solution('KAKAO'))
#print(solution('TOBEORNOTTOBEORTOBEORNOT'))
#print(solution('ABABABABABABABAB'))