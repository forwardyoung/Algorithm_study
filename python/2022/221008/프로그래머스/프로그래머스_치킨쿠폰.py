def solution(coupon):
    answer = 0 # 서비스로 받을 수 있는 치킨 총 몇 마리? 0으로 초기화
    while coupon >= 10: # 쿠폰의 수가 10장 이상이면
        div, mod = divmod(coupon, 10) # coupon을 10으로 나눈 몫과 나머지를 각각 div와 mod에 저장
        answer += div # 위에서 구한 몫이 곧 서비스로 받은 치킨의 수
        coupon = div + mod # 치킨의 수만큼 쿠폰을 받게 되는데 원래 있던 남은 쿠폰을 더한다.
    return answer