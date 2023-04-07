from collections import deque # 시간복잡도 고려
N, M, start = map(int, input().split())
A = [[] for _ in range(N+1)] # 그래프 데이터 저장 인접 리스트 생성 

for _ in range(M): # 에지의 개수만큼 반복
    a, b = map(int, input().split()) 
    A[a].append(b) # 양방향 에지이므로 양쪽에 에지를 더한다
    A[b].append(a)
    
for i in range(N+1):
    A[i].sort() # 번호가 작은 노드부터 방문하기 위해 정렬

def DFS(v):
    print(v, end=' ') # 현재 노드 출력
    visited[v] = True # visited 리스트에 현재 노드 방문 기록
    for i in A[v]:
        if not visited[i]:
            DFS(i) # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행
            
visited = [False] * (N+1) # visited 리스트 초기화
DFS(start)

def BFS(v):
    queue = deque()
    queue.append(v) # 큐 자료구조에 시작 노드 삽입
    visited[v] = True # visited 리스트에 현재 노드 방문 기록
    while queue: # 큐가 비어 있을 때까지
        now_Node = queue.popleft() # 큐에서 노드 데이터 가져오기
        print(now_Node, end=' ') # 가져온 노드 출력
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i) # 현재 노드의 연결 노드 중 미 방문 노드를 큐에 삽입하고 방문 리스트에 기록
print()
visited = [False] * (N+1)
BFS(start)