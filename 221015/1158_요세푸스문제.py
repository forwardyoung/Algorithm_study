# 원형 큐
from collections import deque
N, K = map(int, input().split())

people = deque()
for i in range(1, N+1): people.append(i)
result = []

while people:
  for _ in range(K-1):
    people.append(people.popleft())

  result.append(people.popleft())
# 메서드 replace 사용 : replace('바꿀문자열', '새문자열')
print(str(result).replace('[', '<').replace(']', '>'))