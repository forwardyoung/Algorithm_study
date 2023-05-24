def solution(food):
    temp = '' # 왼쪽=>오른쪽 
    for i in range(1, len(food)):
        temp += str(i) * (food[i] // 2)
    return temp + "0" + temp[::-1] # 가운데는 0이고 temp를 거꾸로 
        