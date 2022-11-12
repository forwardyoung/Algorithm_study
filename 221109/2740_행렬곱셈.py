import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 행렬 A의 크기
A = [list(map(int, input().split())) for i in range(N)]
M, K = map(int, input().split()) # 행렬 B의 크기
B = [list(map(int, input().split())) for i in range(M)]

for i in range(N):
    result = []
    for l in range(K):
        a = 0
        for j in range(M):
            a += A[i][j] * B[j][l]
        result.append(a)
    print(*result)