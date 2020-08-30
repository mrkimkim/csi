import copy

def search(c, idx, words, head, tail):
    if words[head][idx] == c and words[tail][idx] == c:
        return head, tail

    if head >= tail:
        return -1, -1
    
    MID = (head + tail) // 2
    left = search(c, idx, words, head, MID)
    right = search(c, idx,  words, MID + 1, tail)
    
    if left[0] != -1 and right[0] != -1:
        return left[0], right[1]
    if left[0] != -1:
        return left[0], left[1]
    if right[0] != -1:
        return right[0], right[1]
    return -1, -1

def solution(words, queries):
    result = [0] * len(queries)
    used_dic = {}
    dic = {}
    reverse_dic = {}

    words = list(set(words))
    for i in range(len(words)):
        word = words[i]
        length = len(word)
        if length not in dic:
            dic[length] = []
            reverse_dic[length] = []
        dic[length].append(word)
        reverse_dic[length].append(word[::-1])
        
    for key in dic:
        dic[key].sort()
        reverse_dic[key].sort()
        
    used_query = {}
    for i in range(len(queries)):
        orig_query, query = queries[i], queries[i]
        
        if query in used_query:
            result[i] = used_query[query]
            continue
        length = len(query)
        if length not in dic:
            result[i] = 0
            continue
            
        idx = 0
        picked_dic = dic
        if query[0] == '?':
            query = query[::-1]
            picked_dic = reverse_dic
            
        head, tail = 0, len(dic[length]) - 1
        for k in range(length):
            if query[idx] != '?':
                head, tail = search(query[idx], idx, picked_dic[length], head, tail)
                idx += 1
            else:
                break
        if head != -1:
            answer = max(tail - head + 1, 0)
        else:
            answer = 0
        used_query[orig_query] = answer
        result[i] = answer
    return result
