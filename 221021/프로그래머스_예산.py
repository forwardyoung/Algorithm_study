def solution(d, budget):
    answer = 0
    d.sort()
    sum_ = 0
    for i in d:
        if (sum_ + i) <= budget:
            sum_ += i
            answer += 1
    return answer