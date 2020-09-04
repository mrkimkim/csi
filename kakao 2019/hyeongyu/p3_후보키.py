def get_bit_counts(ranges):
    ret = {}
    for i in range(ranges):
        num, cnt = i, 0
        while num > 0:
            cnt += num % 2
            num //= 2

        if cnt not in ret:
            ret[cnt] = []

        ret[cnt].append(i)
    return ret


def is_unique(relation, state):
    lookup_idx = []
    cnt = 0
    while state > 0:
        if state % 2 == 1:
            lookup_idx.append(cnt)
        state //= 2
        cnt += 1

    candidates = set()
    for record in relation:
        candidates.add("".join([str(record[i]) for i in lookup_idx]))
    return len(candidates) == len(relation)


def apply_minimality(is_valid_key, state):
    for i in range(len(is_valid_key)):
        if i & state == state:
            is_valid_key[i] = False
    return


def solution(relation):
    row, col = len(relation), len(relation[0])
    # 가능한 모든 키 사용 조합의 수
    comb = 2 ** col

    # 해당 키 조합이 유효한지를 저장 (-1 : 미정, 0 : 불능, 1 : 유효)
    is_valid_key = [-1] * comb
    # 사용된 키의 수에 따라 키 조합을 분류함.
    bit_count = get_bit_counts(comb)

    # 적은 갯수의 키를 사용하는 것부터 차례대로 탐색
    for cnt in bit_count:
        # cnt 갯수의 키를 사용하는 키 조합들에 대해
        for state in bit_count[cnt]:
            # 아직 초기화 안되었고, 이것들만으로 unique한 키를 만들 수 있으면
            if is_valid_key[state] == -1 and is_unique(relation, state):
                # Minimality를 위해 이 키를 포함하는 다른 키 조합을 모두 비활성화
                apply_minimality(is_valid_key, state)
                is_valid_key[state] = True
            else:
                is_valid_key[state] = False

    # 유효한 키의 갯수를 리턴
    return sum(is_valid_key)