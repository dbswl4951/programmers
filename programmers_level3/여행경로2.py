'''
stack 사용
'''
def solution(tickets):
    graph=dict()
    for start,end in tickets:
        #get(찾을 값, default값)
        graph[start]=graph.get(start,[])+[end]
    #역순 정렬 (맨 뒤부터 pop하기 위해서)
    for key in graph.keys():
        graph[key].sort(reverse=True)
    stack=['ICN']
    path=[]
    while stack:
        top=stack[-1]
        #현재 데이터(top)이 그래프에 있다면, top을 시작점으로 하는 도착점 중 가장 뒤 pop (알파벳 순으로 선택)
        if top in graph and graph[top]:
            stack.append(graph[top].pop())
        #그래프에 없거나, 티켓 모두 사용 한 경우 path에 저장
        else:
            path.append(stack.pop())
    path.reverse()
    return path

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]))
#print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'],['A','C']]))
#print(solution([["ICN", "A"], ["ICN", "A"], ["A", "ICN"]] ))
#print(solution([["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]] ))