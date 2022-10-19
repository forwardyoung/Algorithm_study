def hanoi(num, a, b, c):
    if num == 1:
        move.append([a, c])
    else:
        hanoi(num-1, a, c, b)
        move.append([a, c])
        hanoi(num-1, b, a, c)

move = [] # 이동 경로를 담을 list
num = int(input())
hanoi(num, 1, 2, 3) # 재귀함수

print(len(move)) # 이동 횟수
print("\n".join([' '.join(str(i) for i in row) for row in move])) # 이동 경로 출력
