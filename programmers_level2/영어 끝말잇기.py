def solution(n, words):
    idx=1
    usedWords=[words[0]]
    people=[[] for _ in range(n)]
    people[0].append(words[0])
    flag=0
    while True:
        for i in range(n):
            if idx==1 and i==0 : continue
            people[i].append(words[idx])
            if words[idx-1][-1]==words[idx][0]:
                if words[idx] in usedWords:
                    return [i+1,len(people[i])]
                usedWords.append(words[idx])
            else:
                return [i+1,len(people[i])]
            idx+=1
            if idx>len(words)-1:
                flag=1
                break
        if flag: break
    return [0,0]

#print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
#print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
#print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))