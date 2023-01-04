T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    numbers = [list(map(int, input().split()))
               for _ in range(n)]  # n*n 배열 영역 안에 존재하는 파리의 개수

    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_kill = 0  # 죽인 파리의 개수 누적합
            for k in range(m):
                for l in range(m):
                    sum_kill += numbers[i+k][j+l]
                if sum_kill > result:
                    result = sum_kill  # result값을 sum_kill 값으로 갱신

    print("#{} {}".format(tc, result))
