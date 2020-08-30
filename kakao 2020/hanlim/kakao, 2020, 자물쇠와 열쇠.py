def clockwise(key, m) : # 열쇠 시계방향 90도 회전

    temp = [[0 for i in range(m)] for i in range(m)]

    for i in range(m) :

        for j in range(m) :

            temp[j][m-1-i] = key[i][j]

    return temp

def counterclock(key, m) : # 열쇠 반시계방향 90도 회전

    temp = [[0 for i in range(m)] for i in range(m)]

    for i in range(m) :

        for j in range(m) :

            temp[m-1-j][i] = key[i][j]

    return temp

def clocktwice(key, m) : # 열쇠 180도 회전

    temp = [[0 for i in range(m)] for i in range(m)]

    for i in range(m) :

        for j in range(m) :

            temp[m-1-i][m-1-j] = key[i][j]

    return temp


def findsize(lock, n, m) : # 자물쇠의 홈이 있는 공간의 크기와 위치 도출

    x = []
    y = []

    for i in range(n) :

        for j in range(n) :

            if lock[i][j] == 0 :

                  x.append(i)
                  y.append(j)


    if len(x) == 0 :  # 자물쇠에 홈이 아예 없는 경우(코너해 1)

        return True

    size = max(abs(max(x)-min(x)), abs(max(y)-min(y)))  # x,y 가 없을 수도 있으므로 위의 if 다음에 size 정

    if size > m-1 : # 채워야 할 홈의 영역이 열쇠보다 크다면 불가능(코너해 2)

        return False

    return x, y # 자물쇠의 홈이 있는 곳의 좌표

def findmatch(x, y, key, lock, m, n) : # 자물쇠의 홈과 열쇠의 돌기가 맞물리는지 체크

    h = len(x)
    
    dist_x = 0 
    dist_y = 0

    dxlist = []  # match 되는 좌표들의 거리차이를 저장할 리스트
    dylist = []


    for i in range(m) :  # 자물쇠의 홈을 열쇠로 모두 채울 수 있는가

        for j in range(m) :

            if key[i][j] == 1 :

                dist_x = i - x[0]
                dist_y = j - y[0]


                match = True
                
                for k in range(1,h) :

                    if x[k]+dist_x < 0 or x[k]+dist_x > m-1 or y[k]+dist_y < 0 or y[k]+dist_y > m-1:

                        match = False
                        break

                    elif key[x[k]+dist_x][y[k]+dist_y] == 0 :

                        match = False
                        break

                if match == True : 

                    dxlist.append(dist_x)
                    dylist.append(dist_y)


    a = len(dxlist)

    if a != 0 :  # 주의! match 값을 판정기준으로 삼을 수 없음. match가 True가 되어도 모든 i, j 값에 대해 검토하므로 마지막엔 match 가 False 가 될 수도.

        for k in range(a) :  # 자물쇠와 열쇠가 홈의 나머지 부분에서도 겹쳐질 수 있는가

            allmatch = True
        
            for i in range(n) :

                if allmatch == False :

                    break

                for j in range(n) :

                    if i+dxlist[k] > m-1 or j+dylist[k] > m-1 or i+dxlist[k] < 0 or j+dylist[k] < 0 :  # 자물쇠와 겹치는 열쇠의 부분만 고려

                        continue

                    else :

                        if lock[i][j] + key[i+dxlist[k]][j+dylist[k]] != 1 :

                            allmatch = False
                            break

            if allmatch : # 홈을 다 채우면서 겹쳐진다면 나머지 후보들에 대한 검토 중지하고 결과 반환

                return True
        
        return False


    else :
        return False


def solution(key, lock):

    m = len(key)
    n = len(lock)
    x = []
    y = []


    if not findsize(lock,n,m) :

        return False

    elif findsize(lock,n,m) == True :

        return True

    else : 

        x, y = findsize(lock,n,m)


    if findmatch(x,y,key,lock,m,n) :

        return True

    matrix1 = clockwise(key,m)

    if findmatch(x,y,matrix1, lock,m,n) :

        return True

    matrix2 = counterclock(key,m)

    if findmatch(x,y,matrix2, lock,m,n) :

        return True

    matrix3 = clocktwice(key,m)

    if findmatch(x,y,matrix3, lock,m,n) :

        return True

    return False

    
# Driver program

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))
