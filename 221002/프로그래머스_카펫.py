def solution(brown, yellow):
    a = 0 # 카펫의 넓이(area) 0으로 초기화
    a = brown + yellow # 카펫의 넓이 : 갈색 + 노란 격자의 수를 더한 것
    
    # 테두리 1줄이 brown!
    
    for i in range(a, 2, -1): # 가로
        if a % i == 0:
            h = a // i # h : 세로
            if yellow == (i-2)*(h-2): 
                return [i, h]