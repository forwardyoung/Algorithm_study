n = int(input())
ans = 1 # 경로의 경우의 수 1로 초기화
num = list(map(int, input().split())) # 각 섬에 건설된 다리의 개수 [2, 3, 2]
for i in num: # num 리스트를 순회하며
	ans *= i # ans에 i를 곱하며 저장한다.
	
print(ans)