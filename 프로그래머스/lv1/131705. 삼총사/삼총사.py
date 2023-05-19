from itertools import combinations # 조합
def solution(number):
    answer = 0
    sum_ = list(map(sum, combinations(number, 3)))
    for i in sum_:
        if i == 0:
            answer += 1
    return answer

# 간단하고 pythonic한 코드
# def solution(number):
#     return list(map(sum, combinations(number, 3))).count(0) # map으로 list를 sum함수로 처리 후, count 함수로 0인 요소의 개수를 센다
