from collections import defaultdict
import re


def solution(word, page):

    n = len(page)
    word = word.lower()

    dic = defaultdict(list)   # dic의 내용 : 기본점수, 링크수, 여기로 링크 걸려진 타 사이트 리스트
    
    for i in range(n) :

        page[i] = page[i].lower() # 전부 소문자 변환

        name = findName(page[i])

        if name == None : continue
        
        dic[name].append(countWord(page[i], word))  # 기본점수

        temp = countfromLink(page[i]) # name에서 나가는 링크들의 리스트
        dic[name].append(len(temp)) 
        dic[name].append(temp)   
        dic[name].append([])  # 들어오는 링크를 저장할 리스트 초기화
        dic[name].append(i)  # page의 인덱스를 저장. 딕셔너리는 key의 순서를 관리하지 않음. 


    for key in dic.keys() :

        links = dic[key][2]

        for j in range(len(links)) :

            if links[j] in dic.keys() : # 들어오는 링크는 key 중에 하나일 때만 유의미

                dic[links[j]][3].append(key)

# dic의 구조 [ 기본점수, 링크수, 여기서 나가는 링크 리스트, 여기로 들어오는 링크 리스트, page index ]


    scores = [0]*n

    for origin in dic.keys() :

        basic = dic[origin][0]

        links = dic[origin][3]

        link_points = 0

        for key in links :

            if key == origin : continue  # 자기 자신으로 링크가 걸려 있을 경우 배제

            link_points = float(link_points) + float(dic[key][0]/dic[key][1])

        match_points = float(basic) + link_points
        scores[dic[origin][4]] = match_points  # page 배열의 index 대로 매칭점수 배치

                         
    answer = scores.index(max(scores))

    return answer


def findName(string) :

    target = re.compile(r'<head>(.*)</head>', re.DOTALL) # .은 \n을 배제하므로 옵션 필요

    head = target.findall(string)


    target = re.compile(r'<meta property="og:url" content="https://(.*)"/>')

    temp = target.findall(head[0])

    return temp[0]



def countWord(string, word) : 

    temp = list(re.split('[^a-zA-Z]', string)) # 알파벳 이외의 문자를 기준으로 split

    return temp.count(word)



def countfromLink(string) : # 여기서 나가는 링크

    target = re.compile(r'<a href="https://(.*)">')

    temp = target.findall(string)

    return temp



# Driver program

pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
word = 'Muzi'

print(solution(word,pages))
