def solution(A,B):
    A.sort()
    B=sorted(B,reverse=True)
    result=0
    for i in range(len(A)):
        result+=(A[i]*B[i])
    print(result)
    return result

print(solution([1, 4, 2],[5, 4, 4]))
print(solution([1,2],[3,4]))