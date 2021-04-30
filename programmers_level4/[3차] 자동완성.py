'''
[ 1차 시도 ]
Trie 알고리즘을 사용하려다가, Trie 알고리즘에 익숙하지 않아서
시험장이라면 딕셔너리를 이용해서 풀 것 같아서 딕셔너리를 이용해 풀이
=> 테케 14, 19, 21, 22 시간 초과로 실패

[ 2차 시도]
Trie 알고리즘 사용
'''

class Node:
    def __init__(self,char,data=None):
        self.char=char
        self.data=data
        self.possibleWord=0     # 해당 노드를 거쳐갈 경우, 가능한 글자의 수
        self.children={}

class Trie:
    def __init__(self):
        self.head=Node(None)

    # 문자열 삽입
    def insert(self,string):
        # root node에서 시작
        curr=self.head

        for char in string:
            curr.possibleWord+=1
            if char not in curr.children:
                curr.children[char]=Node(char)
            # 다음 노드로 이동
            curr=curr.children[char]

        # 마지막 글자의 possibleWord도 1로 만들어 줌
        curr.possibleWord+=1
        curr.data=string

    # 문자열이 있는지 찾기
    def search(self,string):
        # root node에서 시작
        curr=self.head

        for char in string:
            # 다음 노드가 있으면 타고 내려간다
            if char in curr.children:
                curr=curr.children[char]
            else: return False

        # 해당 노드까지 내려왔을 때, 만들 수 있는 문자가 1개면 True
        if curr.possibleWord==1: return True
        else: return False

def solution(words):
    tree=Trie()
    # 단어 삽입
    for word in words:
        tree.insert(word)

    result=0
    for word in words:
        find=0      # 단어가 있는지 확인하는 변수
        for i in range(len(word)):
            # 해당 단어가 존재하고, 단어를 만들 수 있는 수가 1개 일 때
            if tree.search(word[:i+1]):
                result+=len(word[:i+1])
                find=1
                break
        # 해당 단어가 여러개 일 때, 존재 하지 않을 때
        if not find:
            result+=len(word)

    return result


# 1차 시도 : 딕셔너리 이용
'''
def solution(words):
    wordDic={}
    for word in words:
        idx=1
        while idx<=len(word):
            w=word[:idx]
            if w in wordDic.keys():
                wordDic[w]+=1
            else: wordDic[w]=1
            idx+=1

    result=0
    for word in words:
        idx,cnt = 1,0
        while idx < len(word):
            w = word[:idx]
            if wordDic[w]==1:
                cnt+=len(w)
                break
            idx+=1
        if cnt==0: result+=len(word)
        else: result+=cnt
    return result
'''

#print(solution(["go","gone","guild"]))
#print(solution(["abc","def","ghi","jklm"]))
#print(solution(["word","war","warrior","world"]))