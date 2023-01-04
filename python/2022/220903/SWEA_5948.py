# https://wikidocs.net/106964
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    # 7개의 서로 다른 수를 numbers라는 리스트에 입력받는다.
    numbers = list(map(int, input().split()))

    result = []  # 3개의 정수의 합을 저장할 리스트 생성

    for value in combinations(numbers, 3):  # numbers에서 숫자 세 개를 뽑은 것 ==> value
        result.append(sum(value))  # 3개의 정수의 합을 result 리스트에 저장한다.

    result = list(set(result))  # result 중복 제거
    result.sort(reverse=True)
    # 내림차순 정렬
    print('#{} {}'.format(tc, result[4]))  # 5번째로 큰 수는 result 리스트의 인덱스 4에 해당
