T = int(input())
for i in range(1, T + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    print('#%d' % i, end=' ')
    for j in range(n) :
        print(data[j], end=' ')
    print()