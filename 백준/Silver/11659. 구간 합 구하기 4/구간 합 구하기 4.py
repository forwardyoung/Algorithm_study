import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split())) # N개의 수
prefix_sum =[0] # 합 배열 변수
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp) # 합 배열 리스트에 추가

for _ in range(M): # M개의 줄에 걸쳐서
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1]) # 합 배열에서 구간 합 구하기