from collections import defaultdict
import re


def solution(word, page):

    n = len(page)
    word = word.lower()

    dic = defaultdict(list)   # dic의 내용 : 기본점수, 링크수, 여기로 링크 걸려진 타 사이트 리스트
    
    for i in range(n) :

        page[i] = page[i].lower() # 전부 소문자 변환

        name = findName(page[i])
        dic[name].append(countWord(page[i], word))  # 기본점수

        temp = countfromLink(page[i]) # name에서 나가는 링크들의 리스트
        dic[name].append(len(temp)) 
        dic[name].append(temp)   
        dic[name].append([])  # 들어오는 링크를 저장할 리스트 초기화


    for key in dic.keys() :

        links = dic[key][2]

        for j in range(len(links)) :

            if links[j] in dic.keys() : # 들어오는 링크는 key 중에 하나일 때만 유의미

                dic[links[j]][3].append(key)

# dic의 구조 [ 기본점수, 링크수, 여기서 나가는 링크 리스트, 여기로 들어오는 링크 리스트 ]


    scores = []

    for key in dic.keys() :

        basic = dic[key][0]

        links = dic[key][3]

        link_points = 0

        for key in links :

            link_points = link_points + float(dic[key][0]/dic[key][1])

        match_points = basic + link_points

        print(type(match_points))

        scores.append(match_points)
        
                         
    answer = scores.index(max(scores))

    return answer


def findName(string) :

    target = re.compile(r'"og:url" content="https://(.*)"')

    temp = target.findall(string)

    return temp[0]



def countWord(string, word) : 

    temp = list(re.split('[^a-zA-Z]', string)) # 알파벳 이외의 문자를 기준으로 split

    return temp.count(word)



def countfromLink(string) : # 여기서 나가는 링크

    target = re.compile(r'<a href="https://(.*)"')

    temp = target.findall(string)

    return temp

