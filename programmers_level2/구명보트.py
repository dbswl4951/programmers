'''
투포인터 문제

예전에 못풀어서 답 보고 풀었었는데, 다시 푸니까 수월하게 풀었다.
주위 할 점은 pop()연산을 사용하면 효율성 테스트를 통과 못한다는 것!
'''
def solution(people,limit):
    people=sorted(people,reverse=True)
    left,ringt=0,len(people)-1
    save=[]
    while left<=ringt:
        if people[left]+people[ringt]<=limit:
            save.append([people[left],people[ringt]])
            left+=1
            ringt-=1
        else:
            save.append([people[left]])
            left+=1
    return len(save)


#print(solution([70, 50, 80, 50]	,100))
#print(solution([70, 80, 50],100))