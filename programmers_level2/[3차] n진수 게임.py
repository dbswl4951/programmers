import string

# 0~9, a~z까지 저장
tmp = string.digits+string.ascii_lowercase

# n =진수로 변환
def convert(num,n):
    q,r=divmod(num,n)
    if q==0: return tmp[r]
    else: return convert(q,n)+tmp[r]

def solution(n, t, m, p):
    numbers=''
    cnt=0
    while len(numbers)<=t*m:
        numbers+=convert(cnt,n)
        cnt+=1
    numbers=numbers.upper()

    result=''
    for i in range(p-1,len(numbers),m):
        if len(result)>=t: break
        result+=numbers[i]

    return result

#print(solution(2,4,2,1))
#print(solution(16,16,2,1))
#print(solution(16,16,2,2))