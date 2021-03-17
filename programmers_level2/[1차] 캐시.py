def solution(cacheSize, cities):
    time=0
    cache=[]    #현재 캐싱 된 도시 저장
    q=[]   #캐싱 된 도시 인덱스 저장
    if cacheSize==0:
        return 5*len(cities)
    for city in cities:
        city=city.lower()
        #cache hit
        if city in cache:
            i=cache.index(city)
            time+=1
            q.remove(i)
            q.append(i)
        #cache miss
        else:
            if len(q)<cacheSize:
                q.append(len(q))
                cache.append(city)
            else:
                i=q.pop(0)
                cache[i]=city
                q.append(i)
            time+=5
    return time

#print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
#print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
#print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
#print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
#print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
#print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
#print(solution(5,['A','A','B','B','A','C']))
#print(solution(4,['B','C','A','D','A']))