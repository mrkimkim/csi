def has_pillar(plot, x, y):
    return (x, y) in plot and plot[(x, y)] & 1 == 1
    
def has_beam(plot, x, y):
    return (x, y) in plot and plot[(x, y)] & 2 == 2

def is_valid_pillar(plot, x, y):
    if y == 0:
        return True
    
    # has pillar below
    if has_pillar(plot, x, y - 1):
        return True
    
    # has beam side
    if has_beam(plot, x - 1, y) or has_beam(plot, x,  y):
        return True
        
    return False

def is_valid_beam(plot, x, y):
    # has pillar below
    if has_pillar(plot, x, y  -1) or has_pillar(plot, x + 1, y - 1):
        return True
    
    # has beam at both side
    if has_beam(plot, x - 1, y) and has_beam(plot, x + 1, y):
        return True

    return False

def is_valid(plot, x, y):
    # empty
    if (x, y) not in plot or plot[(x, y)] == 0:
        return True
    if plot[(x, y)] & 1 == 1 and not is_valid_pillar(plot, x, y):
        return False
    if plot[(x, y)] & 2 == 2 and not is_valid_beam(plot, x, y):
        return False
    return True
        

def is_valid_pillar_operation(plot, x, y):
    return is_valid(plot, x, y) and is_valid(plot, x, y + 1) and is_valid(plot, x - 1, y + 1) and is_valid(plot, x + 1, y + 1)

def is_valid_beam_operation(plot, x, y):
    return is_valid(plot, x, y) and is_valid(plot, x - 1, y) and is_valid(plot, x + 1, y)

def change_pillar(plot, x, y, b):
    if (x, y) not in plot:
        plot[(x, y)] = 0
        
    if has_pillar(plot, x, y) and b == 1:
        return False
    elif not has_pillar(plot, x, y) and b == 0:
        return False
    
    plot[(x, y)] ^= 1
    return True
    
def change_beam(plot, x, y, b):
    if (x, y) not in plot:
        plot[(x, y)] = 0
    if has_beam(plot, x, y) and b == 1:
        return False
    elif not has_beam(plot, x, y) and b == 0:
        return False
    
    plot[(x, y)] ^= 2
    return True
    
def operation(plot, x, y, a, b):
    # pillar
    if a == 0 and change_pillar(plot, x, y, b):
        if is_valid_pillar_operation(plot, x, y):
            return True
        change_pillar(plot, x, y, b^1)
        
    # beam    
    elif change_beam(plot, x, y, b):
        if is_valid_beam_operation(plot, x, y):
            return True
        change_beam(plot, x, y, b^1)
    return False

def solution(n, build_frame):
    plot = {}
    answer = set()
    for frame in build_frame:
        x, y, a, b = frame
        if operation(plot, x, y, a, b):
            if (x, y, a) not in answer:
                answer.add((x, y, a))
            else:
                answer.remove((x, y, a))

    # sort answer and print
    answer = list(answer)
    answer.sort()
    for i in range(len(answer)):
        answer[i] = [answer[i][0], answer[i][1], answer[i][2]]
    return answer

a = solution(100, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print (a)
