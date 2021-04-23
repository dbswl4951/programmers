import copy

def solution(files):
    fileList=[]
    for file in files:
        temp=copy.deepcopy(file)
        idx=0
        while True:
            if temp[idx].isdigit():
                break
            idx+=1
        head=temp[:idx].upper()
        temp=temp[idx:]

        idx=0
        while idx<5:
            if idx<len(temp) and temp[idx].isdigit():
                idx+=1
            else: break
        number=int(temp[:idx])
        tail=temp[idx:]
        fileList.append([head,number,tail,file])

    fileList.sort(key=lambda x:(x[0],x[1]))
    result=[]
    for f in fileList:
        result.append(f[3])
    return result

#print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
#print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
#print(solution(['abc0023005 -cc.zip','gGQ0  .zip']))
#print(solution(['aa32','ac0','c014']))