T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    shape = [list(map(int, input().split())) for _ in range(N)] # list comprehension으로 작성 가능

    result = 0
    cnt = 0
    for i in range(N):

        for j in range(N):
            if shape[i][j] == 1: # [i][j]
                cnt += 1
            if shape[i][j] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt = 0
        for j in range(N):
            if shape[j][i] == 1: # [j][i]
                cnt += 1
            if shape[j][i] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt = 0
    print("#{} {}".format(tc, result))