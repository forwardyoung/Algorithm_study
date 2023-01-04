import sys
input = sys.stdin.readline

K, N = map(int, input().split())
length = []  # K개의 각 랜선의 길이를 담을 리스트

for i in range(K):
    length.append(int(input()))

# 랜선 길이는 1부터 가장 긴 랜선의 길이까지
start = 1  
end = max(length) # 가장 긴 랜선의 길이 => print할 것

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
