## 🙅‍♀️ 자꾸 문제를 제대로 안 읽고 입출력만 보고 문제를 이해하고 있다!
➡️ 조건에 부합하지 않아 테스트 케이스를 통과하지 못하거나 아예 틀리게 된다.


- 출석부의 순서는 이름을 기준으로 사전 순서로 정렬되어 있지만, 이름이 같다면 키가 큰 순서대로 정렬하기로 한다.
- 사람들의 이름과 키가 모두 같은 사람은 없으며, 키는 소수 번째 자리 까지 알고 있다.

```python
통과하지 못한 test case가 있는 코드
N, K = map(int, input().split())
name = []
height = []
for _ in range(N):
	s, t = input().split()
	name.append(s)
	height.append(t)
print(name[K-1], height[K-1])
```

