def solution(A, B):
    result,idx=0,0
    A.sort()
    B.sort()
    for a in A:
        for i in range(idx,len(B)):
            idx += 1
            if a<B[i]:
                result+=1
                break
    return result

#print(solution([5,1,3,7],[2,2,6,8]))
#print(solution([2,2,2,2],[1,1,1,1]))
#print(solution([9,9,9,1],[2,3,4,5]))