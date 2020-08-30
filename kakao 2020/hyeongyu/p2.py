def getFix(s):
    ret = ""
    for i in range(1, len(s) - 1):
        if s[i] == '(':
            ret += ')'
        else:
            ret += '('
    return ret

def isCorrect(s):
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def do(s):
    if len(s) == 0:
        return ""
    i, cnt = 0, 0
    while True:
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        i += 1
        if cnt == 0:
            break
            
    u, v = s[:i], s[i:]
    if isCorrect(u):
        return u + do(v)
    else:
        return '(' + do(v) + ')' + getFix(u)
        

def solution(p):
    return do(p)
