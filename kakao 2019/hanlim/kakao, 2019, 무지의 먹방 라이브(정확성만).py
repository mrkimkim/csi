def solution(food_times, k):

    if sum(food_times) <= k :
        return -1

    n = len(food_times)

    i = 0

    while k > 0 :

        if food_times[i] != 0 :

            food_times[i] = food_times[i] -1
            k -= 1

        i = (i+1) % n

    while food_times[i] == 0 :  # 다음 번 먹어야 할 번호의 음식량이 0인 경우 건너뛰어야 함.

        i = (i+1) % n   # 그냥 i+1 하면 list out of index 때문에 runtime error 발생
    
    return i +1


# Driver code
food_times = [3,1,1,1,2,4,3]
k = 12

print(solution(food_times, k))
