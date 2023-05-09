from collections import deque
from itertools import combinations # itertools.combinations(iterable, r) 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
wall = 0 # 벽의 개수    
blank = [] # 빈 칸 좌표 리스트
virus = [] # 바이러스 좌표 리스트
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0: # 좌표 값이 0이면
            blank.append((i, j)) # 빈 칸 리스트에 위치 추가
        elif matrix[i][j] == 2: # 좌표 값이 2이면
            virus.append((i, j)) # 바이러스 리스트에 위치 추가
        else: 
            wall += 1 # 벽의 개수에 1씩 더하기
wall3 = [] # 3개의 벽 리스트
for i in combinations(blank, 3): # 조합으로 빈 칸 중에 3군데 고르기
    wall3.append(i)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 

def bfs():
    start = deque()
    visit = [[0] * M for _ in range(N)]
    for i in virus:
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
    cnt = 0 # 바이러스가 퍼지지 않은 곳    
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                cnt += 1
    return cnt-wall-3 # wall(벽의 개수)- 내가 세운 벽의 개수 3
result = []
for i in wall3:
    for j in i:
        matrix[j[0]][j[1]] = 1
    result.append(bfs())
    for j in i:
        matrix[j[0]][j[1]] = 0
print(max(result))