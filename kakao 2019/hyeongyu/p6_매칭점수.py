# 페이지의 URL
def get_page_url(page):
    # 범위가 HEAD 태그 내부
    head_start_idx = page.find("<head>")
    meta_start_idx = head_start_idx
    while True:
        # 범위가 Meta 태그 내부, head 태그 내부에서 검색
        meta_start_idx = page.find("<meta", meta_start_idx)
        meta_end_idx = page.find(">", meta_start_idx)
        if meta_start_idx != -1:
            # 모든 url은 https://임, meta 태그 시작 위치 이후로 검색
            content_idx = page.find('https://', meta_start_idx)
            content_end_idx = page.find('"', content_idx)
            # 유효한 인덱스를 찾았고, meta 태그 내부이면
            if content_idx != -1 and content_idx < meta_end_idx:
                return page[content_idx:content_end_idx]
            meta_start_idx = meta_end_idx + 1
        else:
            return ""

# 외부 링크를 찾는다
def get_external_links(page):
    starter = '<a href="https://'
    idx = 0
    links = []
    while True:
        idx = page.find(starter, idx)
        if idx == -1:
            return links
        idx += 9
        end_idx = page.find('"', idx)
        links.append(page[idx:end_idx])
        idx = end_idx + 1
    return links

# 주어진 단어를 대소문자 관계없이, 
def get_word_score(word, page):
    new_page = ""
    for i in range(len(page)):
        if (ord(page[i]) >= 65 and ord(page[i]) <= 90) or (ord(page[i]) >= 97 and ord(page[i]) <= 122):
            new_page += page[i]
        else:
            new_page += " "
    words = new_page.split()

    cnt = 0
    for i in range(len(words)):
        if word.lower() == words[i].lower():
            cnt += 1
    return cnt


def solution(word, pages):
    page_dic = {}
    for i in range(len(pages)):
        page = pages[i]
        page_url = get_page_url(page)
        page_dic[page_url] = [-get_word_score(word, page), i]

    for i in range(len(pages)):
        page = pages[i]
        page_url = get_page_url(page)
        external_links = get_external_links(page)
        word_score = get_word_score(word, page)
        for link in external_links:
            if link in page_dic and link != page_url:
                page_dic[link][0] -= (word_score / len(external_links))

    result = list(page_dic.values())
    result.sort()
    return result[0][1]