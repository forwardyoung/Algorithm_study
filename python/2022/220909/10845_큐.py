import sys
N = int(sys.stdin.readline().rstrip())
queue = []

for _ in range(N):
    command = list(sys.stdin.readline().rstrip().split())

    if command[0] == "push":
        queue.append(command[1])

    elif command[0] == "pop":
        # 제일 앞을 pop 한다.
        print(queue.pop(0) if len(queue) else -1)

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        print(0 if len(queue) else 1)

    elif command[0] == "front":
        print(queue[0] if len(queue) else -1)

    elif command[0] == "back":
        print(queue[-1] if len(queue) else -1)
