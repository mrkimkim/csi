from collections import defaultdict

def solution(words, queries):

    wordict = defaultdict(list)

    for word in words :

        wordict[len(word)].append(word)

    answer = []

    for query in queries :

        n = len(query)
        k = query.count('?')
        count = 0 

        for word in wordict[n] :

            if query[0] == '?' :

                if word[k:] == query[k:] :

                    count += 1

            else :

                if word[:n-k]== query[:n-k] : 

                    count += 1

        answer.append(count)
    
    return answer

# driver program
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))

# 효율성 테스트 1, 2,3, Fail 
