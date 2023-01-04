T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prime_factor = [2, 3, 5, 7, 11]  # 소인수 리스트에 2, 3, 5, 7, 11을 담는다.
    cnt = [0]*5  # 각 소인수 5개의 지수를 담을 빈 리스트 생성

    for n in range(len(prime_factor)):
        while True:
            if N % prime_factor[n] == 0:  # 주어진 숫자 N을 소인수 리스트의 n번째 숫자로 나눈 나머지가 0이면
                N = N//prime_factor[n]  # N은 그 숫자로 나눈 몫
                cnt[n] += 1  # cnt 리스트에서 n번째 인덱스에 1을 더한다.
            else:  # 나눈 나머지가 0이 아니면 멈추고 그 다음 인덱스로
                break
    # 한 칸 공백을 주고 출력해야 하므로 ' '.join
    # .join()은 리스트를 '문자열'로 일정하게 합쳐주는 메서드 ==>  '구분자'.join()으로 사용
    print("#{} {}".format(tc, ' '.join(map(str, cnt))))

    # print("#{} {}".format(tc,cnt)) 이대로 입력하면 #1 [3, 2, 2, 3, 1]과 같이 리스트 형태로 출력된다.
