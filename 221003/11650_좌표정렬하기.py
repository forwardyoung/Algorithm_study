N = int(input())

arr = []
for _ in range(N):
    [x, y] = map(int, input().split())
    arr.append([x, y])

# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력해야 한다.
arr = sorted(arr)

for i in range(N):
    print(arr[i][0], arr[i][1])