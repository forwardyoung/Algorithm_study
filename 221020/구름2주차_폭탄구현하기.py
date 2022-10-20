from collections import deque

n, k = map(int, input().split()) # 한 변의 길이 n, 폭탄의 개수 k
arr = [[0 for _ in range(n)] for _ in range(n)]
q = deque()

dx = [0 ,0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(k):
    a, b = map(int ,input().split()) # 폭탄이 떨어질 위치
    q.append([a-1, b-1])

while q:
    x, y = q.popleft()
    arr[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0  <= nx < n and 0 <= ny < n:
						#해당 과정 대신에, 조건이 성립하면 1을 더해도 된다.
            arr[nx][ny] += 1
ans = 0
for i in arr:
    ans += sum(i)
print(ans)