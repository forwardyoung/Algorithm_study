import sys
input = sys.stdin.readline

N = int(input())
stick = []
for _ in range(N):
	temp = int(input())
	
	stick.append(temp)

cnt = 1
Max = stick[-1]
for i in range(N-1, -1, -1):
	if Max < stick[i-1]:
		cnt += 1
		Max = max(stick[i-1], stick[i])
	
print(cnt)