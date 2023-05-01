import sys
input = sys.stdin.readline

from collections import deque

N, L = map(int, input().split())
d = deque() # 덱 자료 구조 선언
numbers = list(map(int, input().split())) # N개의 수

for i in range(N):
    while d and d[-1][0] > numbers[i]: # 덱이 비어있지 않고 덱의 가장 끝(오른쪽)에 있는 값이 현재 값보다 크면
        d.pop() # 그 값을 덱에서 제거
    d.append((numbers[i], i)) # 덱의 마지막 위치에 현재 값 저장
    if d[0][1] <= i - L: # 덱의 1번째 위치 인덱스가 i - L 보다 작거나 같으면(현재 인덱스 - L >= 인덱스)
        d.popleft() # 1번째 값을 덱에서 제거 - popleft 
    print(d[0][0], end=' ') # 내 덱에서 가장 앞에 있는 데이터의 값 [0][0] 띄어쓰기 하여 출력

