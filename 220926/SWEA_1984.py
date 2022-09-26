# deque => pop으로 풀려고 했으나 결국 문자열 슬라이싱을 이용함
T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    # print(num) [3, 17, 1, 39, 8, 41, 2, 32, 99, 2]
    num.sort()
    # print(num) [1, 2, 2, 3, 8, 17, 32, 39, 41, 99]
    # print("#{} {}".format(tc, sum(num[1:9])//8)) 소수점 첫째 자리에서 반올림해야 하므로 틀림
    print("#{} {}".format(tc, round(sum(num[1:9])/8)))

    # print('#%d %d' % (tc, round(sum(num[1:9])/8))) => 동일한 출력값이 나옴
    # 문자열 중간에 %d가 있으면 파이썬은 이 부분에 정수 타입의 숫자가 올 것을 인식한다.
    # num = 50
    # s = 'my age %d' % num
    # print(s)    