def solution(records):
    answer = []
    dic = {}
    for record in records:
        info = record.split()
        if len(info) == 3:
            identifier, nick = info[1], info[2]
            dic[identifier] = nick

    for record in records:
        info = record.split()
        action, nick = info[0], dic[info[1]]
        if action == "Enter":
            answer.append(nick + "님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(nick + "님이 나갔습니다.")
    return answer
