def solution(d, budget):
    answer = 0
    d.sort()
    sum_ = 0
    for i in d:
        if (sum_ + i) <= budget:
            sum_ += i
            answer += 1
        # 다음 else문은 필수적인 것은 아님!
        # else:
        #     break
    return answer