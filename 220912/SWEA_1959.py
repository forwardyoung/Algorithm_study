T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(input().split())
    b = list(input().split())

    result = 0
    for i in range(abs(n - m) + 1):
        value = 0
        for j in range(min(n, m)):
            if len(a) > len(b):
                value += int(a[j+i]) * int(b[j])
            elif len(a) < len(b):
                value += int(a[j]) * int(b[j+i])
            else:
                value += int(a[j]) * int(b[j])
        if value > result:
            result = value

    print('#%d %d' % (tc, result))
