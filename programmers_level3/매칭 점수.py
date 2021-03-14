from collections import defaultdict
import re

def solution(word, pages):
    basicScore={}   #기본 점수
    linkedScore=defaultdict(int)    #링크 점수
    tagParser=re.compile('a href="(.+)*"')

    for idx,page in enumerate(pages):
        #현재 page url 구함
        pageUrl=page.split('<meta property="og:url" content="')[1].split('"')[0]
        bodyText=page.split('<body>')[1].split('</body>')[0]
        aHrefs=[]   #외부 링크 저장
        for outLinked in page.split('<a href="')[1:]:
            aHrefs.append(outLinked.split('">')[0])
        #body tag 안의 모든 문자열 lower로 바꾸고, 알파벳이 아닌 경우 .로 변경 후, .에 대해 split()
        #re.sub(페턴, 바꿀 문자열, 문자열, 바꿀 횟수) : 문자열 변경
        bodyText=re.sub('[^a-z]+','.',bodyText.lower()).split('.')
        #word를 소문자로 변경 후, bodyText와 매칭 되는 개수 count
        score=len(list(filter(lambda x:x==word.lower(),bodyText)))
        basicScore[pageUrl]=(score,idx)
        #외부 링크 점수 구하기
        for aHref in aHrefs:
            linkedScore[aHref]+=(score/len(aHrefs))

    matchScore=[]
    for key,value in basicScore.items():
        bScore,idx=value[0],value[1]
        lScore=linkedScore[key]
        matchScore.append((idx,bScore+lScore))
    return sorted(matchScore,key=lambda x:(x[1],-x[0]),reverse=True)[0][0]

#print(solution('blind',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))