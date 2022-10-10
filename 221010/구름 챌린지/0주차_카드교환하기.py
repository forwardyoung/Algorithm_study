N, M = map(int, input().split())
num = list(map(int, input().split())) 
# print(num) num이라는 리스트에 N개의 카드 번호들을 담는다.
for _ in range(M):
	u, v = map(int, input().split())
	print(u, v)
    