def solution(s):
    
    n = len(s)

    minn = 1001  
    unit = ""  # 바로 뒤의 문자열 slicing이 같은 문자열인지 비교할 기준
    
    for size in range(1, n//2+2) : # size는 전체 문자열의 절반 + 1 까지만 비교하면 충분
                                   # 문자열 길이가 1인 코너해를 커버하기 위해 +2 해준다.
        unit = s[:size]
        count = 0 
        i = 0
        
        temp = []

        while i+size <= n  : # size 단위로 자를 수 있을 정도의 문자열이 남았는지  check

            if unit == s[i:i+size] : 

                count += 1

            else :
                # 인접한 slicing이 unit과 다르면 그걸 저장
                if count > 1: 
                    temp.append(str(count))

                temp.append(unit)
                count = 1
                #새로운 unit 지정
                unit = s[i:i+size]

            i += size  # 다음 slicing 위해 i 값 증가


        # 루프가 깨지기 직전의 count와 unit 값 append
        if count >1 :
             temp.append(str(count))

        temp.append(unit)

        # 루프를 다 돌고 난뒤 n이 size의 배수가 아니라 남은 잔여물이 있을 경우 append
        if s[i:] != '' :   
            temp.append(s[i:])
        
        minn = min(minn, len("".join(temp)))
            

    return minn
