T = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]  # S마켓에서 사용하는 돈의 종류
for tc in range(1, T+1):
    price = int(input())
    cnt = []  # 각 종류의 돈이 몇 개씩 필요한지 담는 리스트

    for m in money_list:
        cnt.append(price // m)  # 정수 몫(//)으로 price가 32850일 경우, 만원은 3개 필요함을 구한다.
        price %= m  # 금액을 다시 설정할 때 m으로 나눈 나머지가 아닌 마이너스로 해도 된다.
    print(f'#{tc}')
    print(*cnt)
