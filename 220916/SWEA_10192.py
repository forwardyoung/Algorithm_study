T = int(input())

for tc in range(1, T + 1):
    word = list(input())
    word.sort()
    result = []  # 중복을 제거한 문자들을 담을 리스트

    for i in word:
        if result and result[-1] == i:
            result.pop()  # 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
        else:
            result.append(i)

    if len(result) == 0:  # result 리스트의 길이가 0이라면 ==> 모두 for문 첫번째에 해당하면 (xxyyzz의 사례)
        print("#{} {}".format(tc, 'Good'))
    else:
        print("#{} {}".format(tc, ''.join(result)))
