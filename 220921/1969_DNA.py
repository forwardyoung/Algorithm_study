N, M = map(int, input().split())  # N : DNA의 수, M : 문자열의 길이

DNA = []
for _ in range(N):  # N개의 DNA를 입력받는다.
    DNA.append(input())

ans = ''  # Hamming Distance의 합이 가장 작은 DNA
sum_ = 0  # 합이 가장 작은 DNA의 Hamming Distance 합

# 반복문을 통해 서로 다른 4가지의 뉴클레오타이드가 몇 개씩 있는지 확인한다.
for i in range(M):
    count = [0, 0, 0, 0]  # 사전순으로 A, C, G, T의 개수
    for j in range(N):
        if DNA[j][i] == 'A':  # DNA가 'A'라면
            count[0] += 1  # count의 인덱스 번호 0에 1을 더한다.
        elif DNA[j][i] == 'C':  # DNA가 'C'라면
            count[1] += 1  # count의 인덱스 번호 1에 1을 더한다.
        elif DNA[j][i] == 'G':  # DNA가 'G'라면
            count[2] += 1  # count의 인덱스 번호 2에 1을 더한다.
        elif DNA[j][i] == 'T':  # DNA가 'T'라면
            count[3] += 1  # count의 인덱스 번호 3에 1을 더한다.
    idx = count.index(max(count))  # count리스트에서 max(count)의 index를 idx라고 한다.
    if idx == 0:
        ans += 'A'
    elif idx == 1:
        ans += 'C'
    elif idx == 2:
        ans += 'G'
    elif idx == 3:
        ans += 'T'
    # Hamming Distance의 합은 DNA의 개수에서 max(count)를 빼서 구한다.
    sum_ += N - max(count)

print(ans)
print(sum_)
