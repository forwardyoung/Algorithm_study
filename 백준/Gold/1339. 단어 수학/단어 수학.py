N = int(input())

words = []

for _ in range(N):
  words.append(input())

# 딕셔너리 초기화
dict = {}

# 딕셔너리에 알파벳별로 값을 집어 넣어준다.
for word in words:
  root = len(word) - 1
  for i in word:
    if i in dict: # 값이 있는경우 더해준다.
      dict[i] += pow(10, root)
    else: # 없는경우 그대로 넣어준다.
      dict[i] = pow(10, root)
    # 제곱근을 뺴준다.
    root -= 1 

# 딕셔너리 내림차순
dict = sorted(dict.values(), reverse=True)

# 값 계산할 변수 선언
result, m = 0,9

# 값 계산하기
for value in dict:
  result += value * m
  m -= 1

print(result)