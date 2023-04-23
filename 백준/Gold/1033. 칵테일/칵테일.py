N = int(input())
A = [[] for _ in range(N)] # 인접 리스트 생성
visited = [False] * N # 탐색 여부 저장 리스트
graph = [0] * N # 각 노드값 저장 리스트
lcm = 1 # 최소 공배수 1로 초기 설정

def gcd(a, b): # 최대 공약수 함수 구현 a 큰 수, b 작은 수 
    if b == 0:
        return a
    else:
        return gcd(b, a % b) # 재귀 함수 형태

def DFS(v):
    visited[v] = True # 현재 노드 방문 기록
    for i in A[v]:
        next = i[0]
        if not visited[next]: # 현재 노드의 연결 노드 중 방문하지 않은 노드라면
            graph[next] = graph[v] * i[2] // i[1] # 다음 노드 값 = 현재 노드 값 * 비율
            DFS(next) # 재귀 형태

for i in range(N-1): # N-1개의 에지 쌍
    a, b, p, q = map(int, input().split())
    # 인접 리스트에 에지 정보 저장
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q)) # 두 수의 곱을 최대 공약수로 나눈 것으로 최소 공배수 갱신

graph[0] = lcm # 0번 노드에 최소 공배수 저장
DFS(0) # 0번에서 DFS 탐색 수행
mgcd = graph[0]

# DFS 이용해 업데이트 된 graph 리스트의 값들의 최대 공약수 계산
for i in range(1, N):
    mgcd = gcd(mgcd, graph[i])

for i in range(N):
    print(int(graph[i] // mgcd), end=' ') # graph 리스트의 각 값을 최대 공약수로 나눠 출력