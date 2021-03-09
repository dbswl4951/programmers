'''
dfs+백트레킹
'''
def dfs(graph,tLen,result,now):
    result.append(now)
    if len(result)==tLen+1: return True
    if now not in graph:
        result.pop()
        return False
    #now와 연결된 value들 조사
    for _ in range(len(graph[now])):
        next=graph[now][-1]
        #now의 맨 뒤의 요소 삭제
        graph[now].pop()
        if dfs(graph,tLen,result,next):
            return True
        graph[now].insert(0,next)
    result.pop()
    return False

def solution(tickets):
    graph={}
    for start,end in tickets:
        # get(찾을 값, 찾는 값 없으면 default값)
        graph[start]=graph.get(start,[])+[end]
    #value 역순으로 정렬 (맨 뒤부터 pop하기 위해서)
    for key in graph.keys():
        graph[key].sort(reverse=True)
    path=[]
    if dfs(graph,len(tickets),path,'ICN'):
        result=path
    return result

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]))
#print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'],['A','C']]))
#print(solution([["ICN", "A"], ["ICN", "A"], ["A", "ICN"]] ))
#print(solution([["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]] ))