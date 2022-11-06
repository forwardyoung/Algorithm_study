from math import factorial # factorial 모듈 
def solution(n, k): # n : 사람의 수, k : 자연수
    answer = [] 
    num = list(range(1,n+1)) # n명의 사람들의 번호 (1~n번)
    while n != 0:
        fact = factorial(n-1)
        answer.append(num.pop((k-1)//fact)) # k-1을 나눈 몫
        n -= 1
        k %= fact # k를 fact로 나눈 몫
    return answer