import sys
sys.setrecursionlimit(10000) # 또는 10**6
input = sys.stdin.readline
N = int(input())

def is_prime(num): # 소수 판별 함수
  for i in range(2, int(num / 2 + 1)):
    if num % i == 0:
      return False
  return True

def DFS(number): # DFS 구현
  if len(str(number)) == N:
    print(number)
  else:
    for i in range(1, 10):
      if i % 2 == 0: # 짝수라면 탐색 건너뛴다.
        continue
      if is_prime(number * 10 + i): # 소수라면 자릿수 늘린다.
      	DFS(number * 10 + i)

# 일의 자리 소수는 2, 3, 5, 7이므로 다음과 같이 DFS 탐색
DFS(2)
DFS(3)
DFS(5)
DFS(7)