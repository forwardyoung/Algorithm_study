T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    print("#{} {}".format(tc, max(numbers))) # max로 최댓값 구하기