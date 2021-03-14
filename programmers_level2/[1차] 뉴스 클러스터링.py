import math

#다중 집합 구하기
def getSet(s):
    strList=[]
    for i in range(len(s)-1):
        t=s[i:i+2]
        if t.isalpha():
            strList.append(t.lower())
    return strList

#자카드 유사도 구하기
def jacquard(a,b):
    minCount=[]
    aSet,bSet=set(a),set(b)
    inter=aSet&bSet
    for i in inter:
        aCount=a.count(i)
        bCount=b.count(i)
        minCount.append(min(aCount, bCount))
        for j in range(minCount[-1]):
            a.remove(i)
        for j in range(minCount[-1]):
            b.remove(i)
    return math.floor(sum(minCount)/(sum(minCount)+len(a)+len(b))*65536)

def solution(str1, str2):
    a=getSet(str1)
    b=getSet(str2)
    if not a and not b: return 65536
    return jacquard(a,b)

#print(solution('FRANCE','french'))
#print(solution('handshake','shake hands'))
#print(solution('aa1+aa2','AAAA12'))
#print(solution('E=M*C^2','e=m*c^2'))
#print((solution('abccc','ccdefgg')))
#print(solution('AAbbaa_AA','BBB'))
#print(solution('abF+Dddeae','ffedsae'))