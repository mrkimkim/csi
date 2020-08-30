import copy

def solution(n, weak, dist):
    
    a = len(weak)
    b = len(dist)
    
    gap = 200
    pos = 0
    
    for i in range(a) :

        temp = copy.deepcopy(weak)
        minn = 201
        maxx = 0
        
        for j in range(i) : 
            
            temp[j] = temp[j] + n

            minn = min(temp)
            maxx = max(temp)

            if maxx - minn < gap :

                gap = maxx - minn
                pos = i

    for i in range(pos) :

        weak[i] = weak[i] + n

    weak.sort()

    for i in range(a) :

        weak[i] = weak[i] - weak[0]

    dist.sort()

    if dist[-1] >= gap :

        return 1

    else :

        gaplist = []

        for i in range(n) 

            


def findMaxGap(arr) :

    n = len(arr)

    if n ==1 :

        return 0

    if n == 0 :

        return -1

    return max(arr) - min(arr)



        
