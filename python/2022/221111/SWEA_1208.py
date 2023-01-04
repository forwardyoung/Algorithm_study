for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1

    print('#' + str(tc), max(box) - min(box))