from collections import defaultdict


def solution(N, stages):

    remaining_players = len(stages)

    failures = defaultdict(list)
    
    for i in range(1, N+1) :

        players = stages.count(i)

        if remaining_players == 0 or players == 0 :

            failures[0.0].append(i)

        else : 

            ratio = players / remaining_players

            failures[ratio].append(i)

        remaining_players = remaining_players - players


    keys = list(failures.keys())

    for key in keys :
        print(type(key))

    print('keys', keys)
    keys.reverse()

    print('reverse keys', keys)
    answer = []
        
    for key in keys :

        failures[key].sort()
    
        answer.extend(failures[key])


    return answer

# Driver Code

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
