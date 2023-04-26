from collections import deque 

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)] # N개의 줄에 걸쳐서 토마토의 정보를 리스트 형태로 담는다.
queue = deque([]) # 좌표를 넣기 위해 []로 
# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0 # 토마토 모두 익을 때까지의 최소 날짜 담을 변수

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: # 익은 토마토 i,j의 좌표를
            queue.append([i, j]) # 큐에 저장한다
           
def bfs():
    while queue:
        # 토마토 좌표 x, y에 
        x, y = queue.popleft() 
         # 처음 토마토 사분면의 익힐 토마토들을 탐색
        for i in range(4): 
            nx = x + dx[i] # 현재의 x값에 dx[i]를 더한다 => 다음 next x
            ny = y + dy[i]
            # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표의 토마토가 0으로 익지 않아야 함
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0: 
                # 익히고 1을 더해주면서 횟수를 세어주기
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
                
bfs()
for i in graph:
    for j in i:
        if j == 0: # 전체를 탐색했을 때 익지 않은 토마토가 있으면 -1 출력
            print(-1) 
            exit()
    cnt = max(cnt, max(i)) # 다 익혔다면 최댓값이 정답
    
print(cnt - 1) #  리스트에서 제일 큰 값에서 1을 뺀 값을 출력 (리스트를 돌 때 0이 아니라 1에서부터 추가해 올라갔기 때문에)
            
            
        
