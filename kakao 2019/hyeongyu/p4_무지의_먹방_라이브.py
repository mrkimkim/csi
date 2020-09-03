def solution(food_times, k):
    # 각 접시의 음식량과 인덱스를 저장 후 음식량 기준 오름차순 정렬
    for i in range(len(food_times)):
        food_times[i] = [food_times[i], i]
    food_times.sort()

    # 아직 음식이 남아있는 접시의 인덱스를 저장
    remained = set([i for i in range(len(food_times))])

    prev = 0
    # 음식량이 적은 것부터 많은 것 순으로 탐색
    for i in range(len(food_times)):
        # 음식 먹는 방식은 한 바퀴를 쭉 도는 것이므로, 이전 접시를 다 비웠다면
        # 현재 접시에 남은 음식 양은 원래 양과 이전 접시의 차이만큼 남아있다
        delta = food_times[i][0] - prev
        prev = food_times[i][0]
        # 현재 접시에 남은 음식을 다 비운다고 하면 그 양만큼
        # 다른 접시들의 음식도 먹어야한다. 모든 접시들에서 현재 접시의 양만큼을
        # 먹을 수 있을만큼 시간이 남았으면 현재 상태에서 마지막 인덱스를 구할 수
        # 없으므로 접시를 제거하고, 소요되는 시간을 빼준다.
        if k >= delta * len(remained):
            k -= delta * len(remained)
            remained.remove(food_times[i][1])
        else:
            # 완전히 다 비우고도 한 바퀴를 다시 돌 수 없다면 마지막 위치를
            # 나머지 연산으로 구할 수 있다.
            answer = list(remained)[k % len(remained)]
            # 접시의 인덱스가 1부터 시작하므로 보정
            return answer + 1
    return -1