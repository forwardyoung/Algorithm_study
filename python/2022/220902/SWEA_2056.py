T = int(input())
for tc in range(1, T+1):
    date = input()
    year = int(date[:4]) # 년도는 리스트 처음부터 인덱스 3까지 슬라이싱한 것
    m = int(date[4:6]) # 월은 리스트의 인덱스 4, 5 슬라이싱
    d = int(date[6:]) # 일은 리스트의 인덱스 6부터 끝까지 슬라이싱
    
    if m < 1 or m > 12: # 월이 00 이거나 13~ 이면 날짜가 유효하지 않은 것   
        print("#{} {}".format(tc,-1))
        continue

    if m in [1, 3, 5, 7, 8, 10, 12]: # 월이 다음 리스트에 있다면 일수가 1~31일이어야 함
        if d < 1 or d > 31:
            print("#{} {}".format(tc,-1))
            continue

    if m == 2: # 2월이라면 1~28일까지만 가능
        if d < 1 or d > 28:
            print("#{} {}".format(tc,-1))
            continue

    if m in [4, 6, 9, 11]: # 월이 다음과 같다면 1~30일까지만 가능
        if d < 1 or d > 30:
            print("#{} {}".format(tc,-1))
            continue
    
    print("#{} {}".format(tc, "%04d/%02d/%02d" % (year, m, d))) # 날짜 포맷팅 -- % : 명령의 시작, 0 : 채워질 문자, 2 : 총 자릿수, d : 10진수(정수)
