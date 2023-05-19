from itertools import combinations # 조합
def solution(number):
    answer = 0
    sum_ = list(map(sum, combinations(number, 3)))
    for i in sum_:
        if i == 0:
            answer += 1
    return answer