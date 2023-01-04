def solution(lottos, win_nums):
    answer = []
    cnt = 7
    
    # 지워진 숫자(0)가 모두 맞을 경우(최고 순위)
    for i in lottos:
        if i == 0: cnt -= 1
        elif i in win_nums: cnt -= 1
    if cnt > 6: answer.append(6)
    else : answer.append(cnt)
    cnt = 7
    
    # 지워진 숫자가 모두 틀릴 경우(최저 순위)
    for j in lottos:
        if j in win_nums: cnt -= 1
    if cnt > 6: answer.append(6)
    else : answer.append(cnt)
    
    return answer