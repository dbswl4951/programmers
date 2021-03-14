'''
트리 문제는 처음이여서 어떻게 트리를 생성 할지 생각을 못했다
'''
import sys
sys.setrecursionlimit(10 ** 6)

class Tree:
    def __init__(self,dataList):
        #기준 root 노드 잡음
        self.data=max(dataList,key=lambda x:x[1])
        #filter() : 특정 조건을 만족하는 요소들을 iterator 객체로 반환
        #self.data를 기준으로 왼쪽 트리, 오른쪽 트리로 나눔
        leftList=list(filter(lambda x:x[0]<self.data[0],dataList))
        rightList=list(filter(lambda x:x[0]>self.data[0],dataList))
        if leftList:
            self.left=Tree(leftList)
        else:
            self.left=None
        if rightList:
            self.right=Tree(rightList)
        else:
            self.right=None

def order(node,preList,postList):
    #전위 순회 : 현재 노드->왼쪽->오른쪽
    #후위 순회 : 왼쪽->오른쪽->현재 노드
    preList.append(node.data)
    if node.left is not None:
        order(node.left,preList,postList)
    if node.right is not None:
        order(node.right,preList,postList)
    postList.append(node.data)

def solution(nodeinfo):
    answer = []
    postList,preList=[],[]
    root=Tree(nodeinfo)
    order(root,preList,postList)
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, preList)))
    answer.append(list(map(lambda x:nodeinfo.index(x)+1,postList)))
    return answer

#print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	))