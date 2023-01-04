from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
dic = defaultdict()
score = list(map(int, input().split()))
for i in score:
	if abs(i) in dic:
		dic.pop(abs(i))
	else:
		dic[i] = 1
print(sum(dic.keys()))


# 나의 풀이 (시간 초과)
# N = int(input())
# score = list(map(int, input().split()))
# pair = [] # 짝이 있는 숫자들
# for i in score:
# 	if i*(-1) in score:
# 		pair.append(i) # [1, 2, 3, -1, -2, -3]
# solo = set(score)-set(pair)
# print(sum(solo))


# solo부터의 코드를 다음과 같이 바꿔도 시간 초과
# for i in pair:
# 	score.remove(i) # [4, -5]
# print(sum(score))