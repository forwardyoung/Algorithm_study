import sys
input = sys.stdin.readline

N = int(input())

road = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 첫번째 값 더하기
first_cost = road[0] * cost[0]

# 가장 값이 싼 주유소 지정
min_cost = cost[0]

for i in range(1, N-1):
    if min_cost > cost[i]:  # 저장한 주유소 값이 현재 주유소 값 보다 비싸면 바꿔준다.
        min_cost = cost[i]  # 값 싼 주유소로 바꿔주기

    first_cost += min_cost * road[i]

print(first_cost)
