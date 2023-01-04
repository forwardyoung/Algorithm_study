import sys
input = sys.stdin.readline
from collections import deque # 위에서부터 1~n : 문제 풀 때 거꾸로 접근 필요

N = int(input())
arr = list(map(int, input().split())) # 1~3 중 몇 번 기술을 썼는지 입력 받는다. 이때, 가장 마지막은 항상 1번 기술
result = deque()

for i in range(1, N+1): # 1, 2, 3, ..., n 순으로 카드 번호 순회, 기술 사용은 거꾸로
    order = arr.pop() # 기술 하나씩 저장하고 pop
    if order == 1: # 1번 기술이면
        result.appendleft(i) # result 가장 맨 왼쪽에 저장
    elif order == 2: # 2번 기술이면
        result.insert(1, i) # 1번 인덱스(두 번째 카드)에 i 추가
    elif order == 3: # 3번 기술이면
        result.append(i) # 제일 밑에 있는 카드 i를 바닥에
print(*result) # deque() 안의 요소들만 출력