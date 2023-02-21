from collections import deque

dq = deque()
answer = []

N, K = map(int, input().split())

for i in range(1, N+1): # 1부터 N까지의 수
    dq.append(i)
    
while dq:
    for i in range(K-1):
        dq.append(dq.popleft())  # k-1번째 까지의 수를 제거하여 dq에 추가
    answer.append(dq.popleft()) # dq에는 K번째부터의 수이고 가장 왼쪽에 있는 수 K를 answer에 추가
    
print("<",end='') # 줄바꿈 없이 다음 출력
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='') # answer의 맨 뒤의 숫자 인덱싱
print(">")