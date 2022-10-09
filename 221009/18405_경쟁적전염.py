from collections import deque
# BFS
# 번호가 낮은 종류의 바이러스부터 먼저 증식
N, K = map(int, input().split())
graph = []
data = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0: # 어느 위치에 바이러스가 존재한다면
            data.append(graph[i][j], 0, i, j) # 바이러스의 번호, 시간, 위치 X, Y tkqdlq

data.sort()
q= deque(data)

