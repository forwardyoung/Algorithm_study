T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split())) # 10개의 수를 리스트로 입력받는다.
    result = 0 # 홀수만 더한 합 -- 0으로 초기화
    for i in numbers: # 숫자 리스트를 i가 순회할 떄
        if i%2 == 1: # i가 홀수라면
            result += i # result에 더한다.
    print("#{} {}".format(tc, result))