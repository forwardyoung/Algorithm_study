from collections import deque

def solution(maps):
    answer = 0
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우
    N = len(maps) # 미로의 세로 길이
    M = len(maps[0]) # 미로의 가로 길이
    
    # 출발 지점
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                sx, sy = i, j
                
    # 레버 찾기
    def bfs(x, y, end):
        q = deque()
        q.append([x, y])
        visited = [[-1] * M for _ in range(N)] # 방문 여부 리스트 생성
        visited[x][y] = 0
        while q:
            x, y = q.popleft()
            if maps[x][y] == end:
                return [visited[x][y], x, y]
            for dir in direction:
                nx = x + dir[0]
                ny = y + dir[1]
                if 0 <= nx < N and 0 <= ny < M: # 좌표 유효성 검사
                    if visited[nx][ny] == -1:
                        if maps[nx][ny] != 'X': # 벽으로 막혀있지 않다면
                            q.append([nx, ny])
                            visited[nx][ny] = visited[x][y] + 1
        return None
    cnt = bfs(sx, sy, 'L') # 출발지(sx, sy)부터 레버까지의 최단 거리
    if cnt == None: # 이동할 수 없어 cnt 값이 없다면
        return -1 # -1 출력
    answer += cnt[0] 
    cnt = bfs(cnt[1], cnt[2], 'E') # 레버에서 도착지 E까지의 최단 거리
    if cnt == None:
        return -1
    answer += cnt[0] # 레버까지의 거리 + 도착지까지의 거리
    return answer
    
