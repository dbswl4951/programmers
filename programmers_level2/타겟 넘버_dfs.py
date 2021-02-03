result=0
def dfs(idx,target,numbers,val,n):
    global result
    #target에 도달하면 방법의 수(result)+1하고 return
    if n==idx and target==val:
        result+=1
        return
    #numbers의 모든 수를 사용했지만 target을 만들지 못했을 때 바로 return
    if n==idx: return
    #numbers의 모든 수를 아직 다 사용하지 않았다면
    dfs(idx+1,target,numbers,val+numbers[idx],n)
    dfs(idx+1,target,numbers,val-numbers[idx],n)

def solution(numbers, target):
    global result
    dfs(0,target,numbers,0,len(numbers))
    return result

#print(solution([1,1,1,1,1],3))