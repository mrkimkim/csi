def solution(N, stages):
    dic = {}
    # 각 스테이지 별로 실패한 사용자의 수를 집계
    for i in range(len(stages)):
        if stages[i] not in dic:
            dic[stages[i]] = 1
        else:
            dic[stages[i]] += 1

    percentile = []
    cnt = 0
    # 각 스테이지에 대해
    for i in range(N):
        # 한 명도 도달한 사람이 없을 경우
        if (i + 1) not in dic:
            percentile.append([0., i + 1])
        # 여기서 실패한 사용자 수 / (전체 사용자 수 - 이전 단계까지 탈락한 누적 탈락자 수)
        else:
            # 비율 (내림차순), 번호 (오름차순)이므로 비율만 음수로 만들어 줌.
            percentile.append([-dic[i + 1] / (len(stages) - cnt), i + 1])
            # 누적 탈락자 수를 증가
            cnt += dic[i + 1]
    # 비율로 내림차순 정렬, 같은 비율일 경우
    percentile.sort()
    answer = [x[1] for x in percentile]
    return answer
