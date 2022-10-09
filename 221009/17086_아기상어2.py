import sys
from collections import deque


# bfs 탐색
def bfs():
    # 델타탐색
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    while queue:

        x, y = queue.popleft()

        # 델타탐색
        for i in range(8):
            a = x + dx[i]
            b = y + dy[i]

            # 범위 내에 있고 탐색하지 않은 곳이라면 탐색
            if 0 <= a < n and 0 <= b < m:
                if visited[a][b] == 0:
                    # 탐색하기 까지 걸린 이동 횟수를 체크
                    visited[a][b] = visited[x][y] + 1
                    queue.append((a, b))


n, m = map(int, sys.stdin.readline().split())

# 상어가 있는 위치를 확인하고 그래프로 표현
visited = []
queue = deque()
for i in range(n):
    graph = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if graph[j] == 1:
            queue.append((i, j))
    visited.append(graph)

bfs()

# 이동 거리에 최대 값을 구하고 처음 시작값을 뺀다.
dist = 0
for i in range(n):
    for j in range(m):
        dist = max(dist, visited[i][j])

print(dist - 1)