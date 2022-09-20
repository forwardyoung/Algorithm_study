import sys
input = sys.stdin.readline

K, N = map(int, input().split())
length = []  # K개의 각 랜선의 길이를 담을 리스트

for i in range(K):
    length.append(int(input()))

start = 1
end = max(length)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt += length[i] // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
