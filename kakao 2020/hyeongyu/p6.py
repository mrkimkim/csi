def count_people(number):
    cnt = 0
    while number > 0:
        cnt += number % 2
        number //= 2
    return cnt

def process(weak, dist, dp):
    K = []
    for i in range(len(dist)):
        K.append(2 ** i)
        # initial position is always zero
        dp[0][K[i]] = dist[i]
        
    for i in range(1, len(weak)):
        for j in range(len(dp[0])):
            # move from previous state without adding people
            if dp[i - 1][j] >= weak[i] - weak[i - 1]:
                dp[i][j] = dp[i - 1][j] - (weak[i] - weak[i - 1])
            
            # add people from possible previous state
            for k in range(len(dist)):
                if j & K[k] == K[k] and dp[i - 1][j ^ K[k]] >= 0:
                    dp[i][j] = max(dp[i][j], dist[k])
            
    answer = len(dist) + 1
    for j in range(len(dp[0])):
        if dp[len(weak) - 1][j] >= 0:
            new_answer = count_people(j)
            answer = min(answer, new_answer)
            
    return answer != len(dist) + 1 and answer or -1
            
def solution(n, weak, dist):
    k = 2 ** len(dist)
    answer = -1
    for i in range(len(weak)):
        # set this position as start position
        new_weak = [0] * len(weak)
        pivot = weak[i]
        for j in range(i, len(weak)):
            new_weak[j - i] = weak[j]- pivot
        for j in range(i):
            new_weak[j + len(weak) - i] = weak[j] + n - pivot
        
        # DP
        dp = [[-1] * k for j in range(len(new_weak))]
        new_answer = process(new_weak, dist, dp)
        if new_answer != -1:
            answer = answer == -1 and new_answer or min(answer, new_answer)
            
    return answer
