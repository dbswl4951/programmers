import itertools,math

#소수인지 판별
def check(n):
    if n < 2: return False
    k=math.sqrt(n)
    for i in range(2,int(k)+1):
        if n%i==0: return False
    return True

def solution(numbers):
    numbers=list(numbers.strip())
    result = set()
    for i in range(1,len(numbers)+1):
        numbersSet=set(map(''.join,itertools.permutations(numbers,i)))
        for number in numbersSet:
            if check(int(number)):
                result.add(int(number))
    return len(result)

#print(solution("17"))
#print(solution("011"))