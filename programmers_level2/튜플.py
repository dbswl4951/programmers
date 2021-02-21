def solution(s):
    s=(s.replace('{','')).replace('}','')
    tList=list(map(int,s.split(',')))
    tSet=set(map(int,s.split(',')))
    temp=[]
    for t in tSet:
        cnt=tList.count(t)
        temp.append([t,cnt])
    temp=sorted(temp,key=lambda x:-x[1])
    result=[]
    for t in temp:
        result.append(t[0])
    return result

#print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
#print(solution("{{20,111},{111}}"))