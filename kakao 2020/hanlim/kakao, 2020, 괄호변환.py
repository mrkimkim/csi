def solution(string) :

    n = len(string)

    if n == 0 :

        return ""


    if right(string) :

        return string


    for i in range(2, n+1, 2) :

        x = string[:i].count('(')
        y = string[:i].count(')')

        if x == y :

            u = string[:i]
            v = string[i:]
            break   # 여기서 break 안 걸어주면 loop 가 계속 돌아간다.

   
    if right(u) :

        return u + solution(v)

    else :

        m = len(u)

        temp = list(u[1:m-1])

        for i in range(m-2) :
            if temp[i] == ')' : 

                temp[i] = '('

            else :

                temp[i] = ')'

                
        answer = '(' + solution(v) + ')'+"".join(temp)

    return answer
        

        
def right(string) :

    n = len(string)

    count = 0
    minn = 0
    
    for i in range(n) :
        if string[i] == '(' :
            count += 1

        else : count -= 1

        minn = min(minn, count)

    if minn == 0 :

        return True

    return False
