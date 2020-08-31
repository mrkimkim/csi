def get_dict(record):
    ret = {}
    for r in record:
        splited = r.split(' ');
        if splited[0] == "Leave":
            continue
        ret[splited[1]] = splited[2]
    return ret

def transform(record, uid_to_name):
    ret = []
    for r in record:
        splited = r.split(' ');
        if splited[0] == "Enter":
            ret.append(uid_to_name[splited[1]] + "님이 들어왔습니다.")
        elif splited[0] == "Leave":
            ret.append(uid_to_name[splited[1]] + "님이 나갔습니다.")
    return ret
        
def solution(record):
    uid_to_name = get_dict(record)
    return transform(record, uid_to_name)