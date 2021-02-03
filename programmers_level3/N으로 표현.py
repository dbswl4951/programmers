'''
N=2일 때 : N이 1일 때, N이 1일 때 경우의 수를 각각 사칙연산
N=3일 때 : N이 1일 때, N이 2일 때 경우의 수를 각각 사칙 연산
...

N을 n번 사용해서 만들 수 있는 수 :
N을 n번 연달아서 사용할 수 있는 수 U
N을 1번             을 때 SET을 사칙연산한 수들의 집합 U
N을 2번 사용했을 때 SET 과 n-2번 사용했을 때 SET을 사칙연산한 수들의 집합 U
... U
N을 n-1번 사용했을 때 SET 과 1번 사용했을 때 SET을 사칙연산한 수들의 집합
'''
def solution(n, number):
    if n==number: return 1
    # set() * 8개의 list 생성
    s=[set() for _ in range(8)]
    #n을 1~8번까지 이어 붙인 수로 초기화
    for idx,x in enumerate(s,start=1):
        x.add(int(str(n)*idx))
    #일반화
    for i in range(1,8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2!=0: s[i].add(op1//op2)
        if number in s[i]:
            return i+1
    return -1

print(solution(5,12))