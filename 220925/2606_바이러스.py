from collections import deque

num = int(input()) # 컴퓨터의 수
p = int(input()) # 연결된 컴퓨터 쌍의 수
link = {} # 네트워크 상에서 직접 연결된 컴퓨터 번호의 쌍 저장

for _ in range(p):
    a, b = map(int, input().split())
    if a in link:
        link[a].append(b)
    else:
        link[a] = [b]
    if b in link:
        link[b].append(a)
    else:
        link[b] = [a]

# 1번 컴퓨터부터 탐색
queue = deque([1])
visited = [1]
cnt = 0
# 더 이상 연결된 컴퓨터가 없을 때 까지 탐색
while queue:
    q = queue.popleft() 
    if q in link:
        for i in link[q]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                cnt += 1
# 탐색된 컴퓨터의 갯수 출력
print(cnt)