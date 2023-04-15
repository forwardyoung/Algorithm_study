from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
visited = [[0]*M for _ in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

# 다른 풀이
# from collections import deque

# 상하좌우 탐색
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# N, M = map(int, input().split())
# A = [[0]*M for _ in range(N)] # 데이터 저장 행렬
# visited = [[False]*M for _ in range(N)] # 방문 기록 저장 리스트

# for i in range(N):
#     numbers = list(input())
#     for j in range(M):
#         A[i][j] = int(numbers[j])
        
# def BFS(i, j):
#     queue = deque()
#     queue.append((i, j)) # 큐에 시작 노드 삽입
#     visited[i][j] = True # 현재 노드 방문 기록
    
#     while queue:
#         now = queue.popleft() # 큐에서 노드 데이터 가져오기
#         # 상하좌우 탐색
#         for k in range(4):
#             x = now[0] + dx[k]
#             y = now[1] + dy[k]
#             if x >= 0 and y >= 0 and x < N and y < M: # 좌표 유효성 검사
#                 if A[x][y] != 0 and not visited[x][y]: # 해당 데이터의 값이 0이 아니고 방문하지 않은 경우 (1이어야 이동 가능) 
#                     visited[x][y] = True # 방문 기록
#                     A[x][y] = A[now[0]][now[1]] + 1 # A 리스트에 depth를 현재 노드의 depth + 1로 업데이트
#                     queue.append((x, y)) # 큐에 데이터 삽입
 
# BFS(0, 0)
# print(A[N-1][M-1])
