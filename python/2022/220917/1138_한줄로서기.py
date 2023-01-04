import sys
input = sys.stdin.readline

N = int(input())
cnt = list(map(int, input().split()))  # 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지 리스트로 입력
answer = [0]*N  # N명의 사람

for i in range(N):
    for j in range(N):
        if cnt[i] == 0 and answer[j] == 0:
            answer[j] = i + 1  # i가 0부터 시작하므로 1을 더해준다
            break
        elif answer[j] == 0:
            cnt[i] -= 1
print(' '.join(map(str, answer)))
