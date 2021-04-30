'''
[ 1차 시도 : 문자열로만 풀기 ]
효율성 테케 1,2,3 시간초과로 실패

[ 2차 시도 : Trie 알고리즘 ]
1) '?'가 앞에 있는지, 뒤에 있는지 나눠서 생각 (Trie는 문자열 앞부터 search하므로)
2) Node에 length를 딕셔너리로 생성
 length = {key:value}
 key : 해당 노드~끝까지 남은 글자 수
 value : key를 만족하는 문자열이 몇 개 있는지

3) key만큼 '?'의 개수(wild)가 남아 있어야지 매치 된 것!
'''

# 2차 시도 (Trie 알고리즘 사용)
class Node:
    def __init__(self,data=None):
        self.data=data
        self.children={}
        # key : 문자열 끝까지 남은 글자 수, value : key에 해당하는 문자열의 개수
        self.length={}

class Trie():
    def __init__(self):
        self.head=Node(None)

    def insert(self,string):
        curr=self.head
        sLen=len(string)

        if sLen not in curr.length:
            curr.length[sLen]=1
        else:
            curr.length[sLen]+=1

        for char in string:
            if char not in curr.children:
                curr.children[char]=Node(char)
            # 다음 노드로 이동
            curr=curr.children[char]
            # 다음 문자열로 이동 => 문자 길이 -=1
            sLen-=1
            if sLen not in curr.length:
                curr.length[sLen]=1
            else:
                curr.length[sLen]+=1

    def search(self,string,wild):
        curr=self.head

        # 자식노드로 string의 끝까지 내려가기
        for char in string:
            if char in curr.children:
                curr=curr.children[char]
            else: return 0

        # 뒤에 오는 ?의 개수가 맞는 것이 없으면 False return
        if wild not in curr.length: return 0
        # 뒤에 오는 ?의 개수가 맞는 것의 수만큼 return
        return curr.length[wild]


def solution(words, queries):
    tree1=Trie()
    tree2=Trie()

    for word in words:
        tree1.insert(word)
        tree2.insert(word[::-1])

    result=[]
    for query in queries:
        if query[0]!='?':
            idx=query.index('?')
            string=query[:idx]
            wild=len(query[idx:])   # ?의 개수
            result.append(tree1.search(string,wild))

        else:
            query=query[::-1]
            idx=query.index('?')
            string = query[:idx]
            wild = len(query[idx:])  # ?의 개수
            result.append(tree2.search(string, wild))
    return result


# 1차 시도 (문자열로만 풀기)
# => 정확성 만점. 효율성 테케 1,2,3 실패 (시간 초과)
'''
def solution(words, queries):
    words=set(words)
    result=[]
    for query in queries:
        cnt=0
        for word in words:
            if len(query)!=len(word): continue
            else:
                idx,flag=0,0
                while idx<len(query):
                    if query[idx]=='?':
                        idx+=1
                        continue
                    if word[idx]!=query[idx]:
                        flag=1
                        break
                    idx+=1
                if not flag: cnt+=1
        result.append(cnt)
    return result
'''

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))