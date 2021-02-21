'''
크루스칼 알고리즘 사용 O(ElogE)
구현 방법이 생각 안나서 전에 풀었던 문제 풀이 참고
'''
#부모 찾기
def find(parent,a):
    if parent[a]!=a:
        parent[a]=find(parent,parent[a])
    return parent[a]

#집합 합치기
def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a<b: parent[b]=a
    else: parent[a]=b

def solution(n, costs):
    parent=[0]*n
    #부모를 자기 자신으로 초기화
    for i in range(n):
        parent[i]=i
    edges=[]
    for a,b,c in costs:
        edges.append((c,a,b))
    #비용 오름차순으로 정렬
    edges.sort()
    result=0
    for c,a,b in edges:
        if find(parent,a)!=find(parent,b):
            union(parent,a,b)
            result+=c
    return result

#print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
#print(solution(5,[[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]))