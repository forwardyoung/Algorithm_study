from collections import deque
 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
def bfs(a, b):
    sheep = 0 
    wolf = 0
 
    queue = deque()
    queue.append((a, b))
 
    if graph[a][b] == 'o':
        sheep += 1
    elif graph[a][b] == 'v':
        wolf += 1
 
    graph[a][b] = '#'
 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#":
                if graph[nx][ny] == 'o':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1
 
                graph[nx][ny] = '#'
                queue.append((nx, ny))
 
    if wolf >= sheep:
        return 0, wolf
    elif sheep > wolf:
        return sheep, 0
 
 
 
 
r, c = map(int, input().split())
graph = []
 
cnt_s = 0 # 전체 sheep의 수
cnt_w = 0 # 전체 wolf의 수 
 
for i in range(r):
    graph.append(list(input()))
 
for i in range(r):
    for j in range(c):
        if graph[i][j] in 'ov':
            tempSheep, tempWolf = bfs(i, j)
            cnt_s += tempSheep
            cnt_w += tempWolf
 
print(cnt_s, cnt_w)