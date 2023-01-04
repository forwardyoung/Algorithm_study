T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total = N * N
    arr = [[0] * N for _ in range(N)]
    cnt = 1
    # 시작은 좌측 상단
    r = 0
    c = 0
    dr = [0, 1, -1, 0]
    dc = [1, 0, 0, -1]
    # 오른쪽이 시작이므로 시작점은 0
    now = 0
    while cnt <= total:
        # 범위를 벗어나지 않고 그 안의 숫자가 0일 때
        if 0 <= r < N and 0 <= c < N and not arr[r][c]:
            arr[r][c] = cnt
            cnt += 1
        else:
            # 더해서 초과된 부분을 다시 빼줌
            r -= dr[now]
            c -= dc[now]
            # 인덱스 초과 방지
            now = (now+1) % 4
        r += dr[now]
        c += dc[now]
    print('#{}'.format(tc))  # print(f'#{tc}')와 동일한 코드
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
