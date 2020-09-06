def isAlpha(c):
    return (ord('a') <= ord(c) <= ord('z'))

def getBasePoint(word, page):
    pos = 0
    count = 0
    while True:
        pos = page.find(word, pos)
        if pos == -1:
            break
        if (pos == 0 or not isAlpha(page[pos-1])) and ( (pos + len(word) == len(page)) or not isAlpha(page[pos+len(word)]) ):
            count += 1
        pos += 1
    return count

def getURL(page):
    return page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]

def getLinkPoint(page, index, link_to_idx, base_points, points):
    ahref = page.split('<a href=\"')[1:]
    total = len(ahref)
    for item in ahref:
        link = item.split('\"')[0]
        if link in link_to_idx:
            points[link_to_idx[link]] += (1 / total) * base_points[index]
    return

def solution(word, pages):
    base_points = [0.0 for i in pages]
    points = [0.0 for i in pages]
    link_to_idx = {}
    word = word.lower()

    for i in range(len(pages)):
        pages[i] = pages[i].lower().replace('\n',' ').replace('\b', ' ').replace('\t', ' ')
        link_to_idx[getURL(pages[i])] = i
        base_points[i] += getBasePoint(word, pages[i])
        points[i] += base_points[i]
    
    for i, page in enumerate(pages):
        getLinkPoint(page, i, link_to_idx, base_points, points)

    max_point = -1.0
    max_index = -1
    for i, v in enumerate(points):
#        print(i, v)
        if max_point < v:
            max_point = v
            max_index = i

    return max_index