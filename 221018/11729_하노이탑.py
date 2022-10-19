def hanoi(num, a, b, c):
    if num == 1: # 원판 num이 1이면
        print(a, c) # a에서 c로 바로 이동할 수 있으므로 이동 경로 a, c를 출력한다.
    else: # 원판 num이 1이 아니라면
        hanoi(num-1, a, c, b) # n-1개의 원판을 a에서 c를 거쳐 b의 장대로 이동시킨다.
        print(a, c) # 원판 num이 a에서 c로 이동하는 경로 a, c를 출력한다.
        hanoi(num-1, b, a, c) # n-1개의 원판을 b에서 a를 거쳐 c로 이동시킨다.

num = int(input())
print(2**num -1) # 이동 횟수
hanoi(num, 1, 2, 3) # a, b, c = 1, 2, 3

# 다른 풀이
# def hanoi(num, a, b, c):
#     if num == 1:
#         move.append([a, c])
#     else:
#         hanoi(num-1, a, c, b)
#         move.append([a, c])
#         hanoi(num-1, b, a, c)

# move = [] # 이동 경로를 담을 list
# num = int(input())
# hanoi(num, 1, 2, 3) # 재귀함수

# print(len(move)) # 이동 횟수
# print("\n".join([' '.join(str(i) for i in row) for row in move])) # 이동 경로 출력