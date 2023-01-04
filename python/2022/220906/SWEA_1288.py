# 풀이 1
T = int(input())

for tc in range(1, T+1):
    numbers = input()
    numbers = numbers.split()  # 띄어쓰기 기준으로 앞, 뒤로 자른다.
    numbers = list(map(int, numbers))  # list로 숫자들을 담는다.

    n_numbers = []
    cnt = 0
    result = 0
    check = [0 for _ in range(10)]

    while True:
        for number in numbers:                          # ex) nubmers = [1295]
            cnt += 1
            # ex) n_numbers = 1295 * 1 = 1295
            n_numbers = cnt * number
            for i in map(int, str(n_numbers)):
                # ex) i = 1, 2, 9, 5 // check[1] = 1 , check[2] = 1...
                check[i] = 1

        # ex) check의 모든 리스트가 1이면 sum()이 10이므로, 종료.
        if sum(check) == 10:
            result = n_numbers
            break

    print(f'#{tc} {result}')

# 풀이 2
T = int(input())

for tc in range(1, T+1):
    n = input()  # 1 문자열로 입력받음
    value = int(n)  # 정수형으로 바꿔줌
    data = [0]*10  # 0이 10개인 리스트 만들어줌 # 0~9까지 다 있는 단계의 값을 구하는 것!
    # data = [0, 1, 2, 3 ]
    while True:  # 범위 없이 반복
        for i in range(len(n)):  # 문자열 길이만큼 반복 즉, 9까지는 1번반복
            data[int(n[i])] += 1  # 문자열의 0번째의 값을 정수형으로 바꿔서, 데이터 배열 자리값에 1을 추가해줌
        if not data.count(0):  # 추가해준 것에서 0이 없을 때 출력하고 반복문 멈춤
            print(f'#{tc} {int(n)}')
            break

        n = str(value+int(n))
