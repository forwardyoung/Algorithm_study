# https://wikidocs.net/106964
from itertools import combinations

T = int(input())
for tc in range(1, T+1) :
    numbers = list(map(int, input().split()))
    result = []
    for value in combinations(numbers, 3) :
        result.append(sum(value))

    result = list(set(result))
    result.sort(reverse=True)
    print('#{} {}'.format(tc, result[4]))