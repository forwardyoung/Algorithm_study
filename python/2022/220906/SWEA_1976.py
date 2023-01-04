T = int(input())
h = 0
m = 0
for tc in range(1, T+1):
    numbers= list(map(int, input().split()))
    h = numbers[0] + numbers[2] # 0, 2번째 인덱스 값을 더한 것이 시
    m = numbers[1] + numbers[3] # 1, 3번째 인덱스 값을 더한 것이 분

    # 다음 두 조건을 충족시켜야 하는데, 순서가 바뀌면 모든 tc를 다 충족하지 못함!
    
    # 두 개의 '분'을 더한 m이 60이상이면, 시를 계산하고 남은 분을 받아들여야 함.
    if m > 59:
        m -= 60
        h += 1 # 60분 이상이면 1시간 증가
    
    # 단, 12시간제이므로 h가 13이 나오면 1으로 표기해야 함.
    if h > 12:
        h -= 12

    print(f"#{tc} {h} {m}")