T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    for _ in range(N):
        shape = list(map(int, input().split()))
    # shape = [list(map(int, input().split())) for _ in range(N)] list comprehension으로 작성 가능
    