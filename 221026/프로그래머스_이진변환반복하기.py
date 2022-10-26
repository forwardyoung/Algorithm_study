def solution(s):
    answer = [0,0] # 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수
    cnt, zero = 0,0
    while True:
        if s == "1":
            break
        else:
            zero += s.count("0")
            s = format(len(s.replace("0","")),"b")
            cnt += 1
    answer[0] = cnt
    answer[1] = zero
    
    return answer