N = int(input()) # 컴퓨터의 수
l = int(input()) # 연결된 컴퓨터 쌍의 수
graph = [[] for _ in range(N+1)] # 그래프 초기화
visited = [0]*(N+1) # 방문 리스트 생성
for _ in range(l):
    a, b = map(int, input().split()) 
    graph[a].append(b) # a에 b연결
    graph[b].append(a) # b에 a연결 - 양방향
def dfs(n):
    visited[n] = 1 # 탐색과 동시에 방문 표시
    for i in graph[n]: # n번 컴퓨터에 연결된 컴퓨터 리스트를 순회
        if visited[i] == 0: # i를 방문하지 않았다면
            dfs(i) # i를 탐색
dfs(1) # 1번부터 
print(sum(visited)-1) # 1을 제외한 컴퓨터의 수
