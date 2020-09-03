def solution(relation):

    column_number = len(relation[0])
    row_number = len(relation)

    variations = 2**(column_number)
    visited = [False] * variations    

    for i in range(1, variations) :

        subset = list(format(i, 'b'))  # 숫자를 2진법으로 표현 0은 비포함, 1은 포함
        m = len(subset)

        if m < column_number :

            subset = ['0']*(column_number - m) + subset  # 길이 통일


        test = set()

        for j in range(row_number) :

            case = tuple()

            for k in range(column_number) :

                if subset[k] == '1' :
                    
                    case = case + (relation[j][k],)  # 원소가 1개인 튜플은 마지막에 콤마를 넣어줘야 한다.

            test.add(case)

        b = len(test)

        if b == row_number :

            visited[i] = True



    for i in range(1, variations) :

        for j in range(i+1, variations) :

            if i & j == i and visited[i] == True and visited[j] == True :

                visited[j] = False

    answer = visited.count(True)
 
    return answer

# Driver Code

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))

