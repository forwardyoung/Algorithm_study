# test case 7개 중 5개만 pass한 풀이 -- A, B 회사의 요금을 비교하여 더 작은 것 출력하는 코드를 입력해야 함!
# T = int(input())
# for tc in range(1, T+1):
#     p, q, r, s, w = map(int, input().split())
#     if w <= r:
#         print("#{} {}".format(tc, p*w))
#     else:
#         print("#{} {}".format(tc, q+(w-r)*s))

T = int(input())
for tc in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    fee_a, fee_b = 0, 0   # A, B 회사의 요금을 0으로 초기화
    fee_a = p*w  # 1L당 요금 p에 사용량 w 곱해준다.
    fee_b += q  # 기본 요금 q가 청구된다.
    if w > r:  # 사용량 w가 기준량 r보다 크다면
        fee_b += (w-r)*s  # q로 저장된 기본 요금에 초과량에 대한 1리터당 s원을 더 내야 한다.
    print("#{} {}".format(tc, min(fee_a, fee_b)))  # 요금이 더 저렴한 회사를 골라 출력 => min
