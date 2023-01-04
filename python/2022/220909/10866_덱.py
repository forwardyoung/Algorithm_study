from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
d = deque()
for _ in range(N):
    order = list(input().split())

    if order[0] == 'push_front':
        d.appendleft(order[1])

    elif order[0] == 'push_back':
        d.append(order[1])

    elif order[0] == 'pop_front':
        if d:
            x = d.popleft()
            print(x)
        else:
            print(-1)

    elif order[0] == 'pop_back':
        if d:
            x = d.pop()
            print(x)
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(d))

    elif order[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)

    elif order[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)

    else:
        print('예외')
