from collections import deque

N, K = map(int, input().split())
dq = deque(range(1, N+1))
ans = list()

while len(dq) > 0:
    dq.rotate(-K+1)
    ans.append(dq.popleft())
    
print(f"<{str(ans)[1:-1]}>")