import sys
input = sys.stdin.readline

N = int(input()) # 정수 N 입력 받는다.

def fact(N):
    if N <= 1: # 1보다 작으면
        return 1 # 1 리턴
    else:
        return N * fact(N-1)
print(fact(N))