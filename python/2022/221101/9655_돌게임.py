# DP 문제이지만 더 간단하게 풀었음

N = int(input())
if N%2 == 1: # N이 홀수면 상근 1 창영 3 상근 1 or 상근 3 창영 1 상근 1 
    print('SK') # 상근이가 무조건 이긴다.
else: # N이 짝수면 상근 1 창영 3 or 상근 1 창영 1 상근 1 창영 1 
    print('CY') # 창영이가 무조건 이긴다.