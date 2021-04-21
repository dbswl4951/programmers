def solution(record):
    dic=dict()
    for re in record:
        r=re.split()
        if r[0]=='Enter' or r[0]=='Change':
            dic[r[1]]=r[2]
    result=[]
    for re in record:
        r = re.split()
        if r[0]=='Enter':
            temp=dic[r[1]]+'님이 들어왔습니다.'
            result.append(temp)
        elif r[0]=='Leave':
            temp=dic[r[1]]+'님이 나갔습니다.'
            result.append(temp)
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))