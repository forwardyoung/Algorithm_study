from itertools import combinations
N, M =map(int, input().split())
arr = combinations(range(1, N+1), M) 
for i in arr:
    # print(i) (1, 2, 3, 4)
    print(' '.join(map(str, i))) # tuple에서 숫자만 출력 