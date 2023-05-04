from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
one = 0
zero = []
two = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            zero.append((i, j))
        elif matrix[i][j] == 2:
            two.append((i, j))
        else:
            one += 1
zero3 = []
for i in combinations(zero, 3):
    zero3.append(i)
count = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]
def bfs():
    start = deque()
    visit = [[0] * M for _ in range(N)]
    for i in two:
        start.append(i)
        visit[i[0]][i[1]] = 2
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = 2
                    start.append((nx, ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                cnt += 1
    return cnt-one-3
result = []
for i in zero3:
    for j in i:
        matrix[j[0]][j[1]] = 1
    result.append(bfs())
    for j in i:
        matrix[j[0]][j[1]] = 0
print(max(result))