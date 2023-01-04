N, M = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line) # matirx = [['1', '2', '4'], ['8', '16', '32']]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum = 0 # 배열의 합 0으로 초기화
    for row in range(i-1, x): # 행은 i부터 x까지의 범위
        for col in range(j-1, y): # 열은 j부터 y까지의 범위
            sum += matrix[row][col]
    print(sum)