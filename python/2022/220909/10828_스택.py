import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    command = input().split()  # 명령이 N개의 줄에 하나씩 주어진다.
    if command[0] == 'push':  # 명령 입력의 첫번째 인덱스 값이 push면
        stack.append(int(command[1]))  # 명령의 [1] 인덱스 숫자값을 stack 리스트에 추가
    elif command[0] == 'top':  # 명령 입력의 첫번째 인덱스 값이 top이면
        if len(stack) > 0:
            print(stack[-1])  # 스택의 가장 위에 있는 정수 출력
        else:
            print(-1)  # 스택에 들어있는 정수가 없으면 -1 출력
    elif command[0] == 'pop':  # 명령의 첫번째 인덱스 값이 pop이면
        if len(stack) > 0:
            print(stack.pop())  # 스택에서 가장 위에 있는 정수를 pop으로 뺀다.
        else:
            print(-1)  # 스택에 들어있는 정수가 없으면 -1 출력
    elif command[0] == 'size':  # 명령의 첫번째 인덱스 값이 size면
        print(len(stack))  # 스택에 들어있는 정수의 개수 출력
    elif command[0] == 'empty':  # 명령의 첫번째 인덱스 값이 empty면
        if len(stack) > 0:
            print(0)  # 0을 출력
        else:
            print(1)  # 스택이 비어있으면 1을 출력
