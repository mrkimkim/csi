def solution(s):
    min_len = len(s)
    for i in range(1, len(s)):
        length = 0
        prev = ""
        idx = 0
        while idx < len(s):
            token = s[idx:min(idx+i, len(s))]
            idx += len(token)
            cnt = 1
            length += len(token)
            while idx + i <= len(s) and token == s[idx:idx + i]:
                idx += i
                cnt += 1
            if cnt > 1:
                length += len(str(cnt))
        if length < min_len:
            min_len = length
    return min_len
