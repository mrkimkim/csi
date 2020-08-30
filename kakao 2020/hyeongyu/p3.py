def isMatch(key, lock, lock_x, lock_y, key_x, key_y, size_x, size_y, goal):
    cnt = 0
    for i in range(size_x):
        for j in range(size_y):
            if lock[lock_x + i][lock_y + j] ^ key[key_x + i][key_y + j] == 0:
                return False
            if key[key_x + i][key_y + j] == 1:
                cnt += 1
    return cnt == goal

def backtracking(key, lock, goal):
    M, N = len(key), len(lock)
    for i in range(0, N + M - 1):
        for j in range(0, N + M - 1):
            lock_x = max(i - M + 1, 0)
            lock_y = max(j - M + 1, 0)
            start_x = lock_x - (i - M + 1)
            start_y = lock_y - (j - M + 1)
            size_x = min(i, N - 1) - max(i - M + 1, 0) + 1
            size_y = min(j, N - 1) - max(j - M + 1, 0) + 1
            if isMatch(key, lock, lock_x, lock_y, start_x, start_y, size_x, size_y, goal):
                return True
    return False
            
def rotate(key):
    M = len(key)
    new_key = [[0] * M for i in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[M - 1 - j][i] = key[i][j]
    return new_key

def solution(key, lock):
    Sum = sum(sum(line) for line in lock)
    if Sum == len(lock) ** 2:
        return True
    goal = len(lock) ** 2 - Sum
    for i in range(4):
        if backtracking(key, lock, goal):
            return True
        key = rotate(key)
    return False
