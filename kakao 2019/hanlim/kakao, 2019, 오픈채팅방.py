from collections import defaultdict


def solution(record):


    n = len(record)

    names = defaultdict(list)


    for i in range(n) :

        a = record[i].split()

        if len(a) == 3 :

            names[a[1]].append(a[2])

        else : continue


    answer = []

    for i in range(n) :

        a = record[i].split()

        if a[0] == 'Enter' :

            answer.append(names[a[1]][-1]+'님이 들어왔습니다.')

        elif a[0] == 'Leave' :

            answer.append(names[a[1]][-1]+'님이 나갔습니다.')

        else : continue
    

    return answer

# Driver Code
record =["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))
