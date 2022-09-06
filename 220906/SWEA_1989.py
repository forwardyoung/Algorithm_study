T = int(input())
for i in range(1, T + 1):
    w = input()
    r = w[::-1]
    if w == r:
        print('#{} {}'.format(i, 1))
    else:
        print('#{} {}'.format(i, 0))