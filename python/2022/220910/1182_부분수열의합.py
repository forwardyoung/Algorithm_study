N, S = map(int, input().split())
array = list(map(int, input().split()))  # N개의 정수로 이루어진 수열 리스트로 입력
count = 0  # 합이 S가 되는 부분수열의 개수를 셀 count값 저장
out = []  # 재귀를 돌면서 위의 array에서 m개를 뽑아서 저장할 리스트 선언


def dfs(depth, idx, m):
    global count

    if depth == m:  # 만약 out 리스트에 m개만큼 추가되었다면
        if sum(out) == S:  # out리스트의 합이 S와 같다면
            count += 1  # count값 1증가
        return

    for i in range(idx, N):  # 인자로 전달받은 idx부터 N까지 돈다.(이전에 돌았던 인덱스는 순회하지 않기 위함)
        out.append(array[i])  # out에 array배열의 값 한 개를 추가
        dfs(depth + 1, i + 1, m)  # 그 후 또 dfs를 돈다.
        out.pop()  # 다 돌았다면 그 값을 out 리스트에서 제거


# 입력받은 array리스트에서 j(1개~N개)의 개수만큼 원소를 뽑는다.
for j in range(1, N + 1):
    dfs(0, 0, j)

print(count)  # count값 출력
