from collections import deque

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    #시작 지점
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                sx, sy = i, j

    visited = [[0 for _ in range(len(maps[0])) ] for _ in range(len(maps))]
    visited[sx][sy] = 1 #시작 지점은 방문 처리

    que = deque([(sx,sy,0)])
    lx = 0 
    ly = 0
    cnt = 0
    flag = False
    while que: #레버까지 가는데 최단 시간
        x,y,cnt = que.popleft()
        if maps[x][y] == "L":
            lx, ly = x, y
            flag = True
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= len(maps) or ny >= len(maps[0]) :
                continue
            if visited[nx][ny] == 1 or maps[nx][ny] == 'X':
                continue

            que.append((nx,ny,cnt + 1))
            visited[nx][ny] = 1

    if flag == False :
        return -1
    visited = [[0 for _ in range(len(maps[0])) ] for _ in range(len(maps))]
    que2 = deque([(lx,ly,cnt)])
    visited[sx][sy] = 0
    while que2: #종료까지 가는데 최단 시간
        x,y,cnt = que2.popleft()
        if maps[x][y] == "E":
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= len(maps) or ny >= len(maps[0]) :
                continue
            if visited[nx][ny] == 1 or maps[nx][ny] == 'X':
                continue

            que2.append((nx,ny,cnt + 1))
            visited[nx][ny] = 1


    return -1