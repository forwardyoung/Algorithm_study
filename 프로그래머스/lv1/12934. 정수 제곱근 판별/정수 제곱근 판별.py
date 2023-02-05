def solution(n):
    square_root = n**(1/2) # n의 1/2거듭제곱은 곧 n의 제곱근
    
    if int(square_root) == square_root: # n의 제곱근이 정수인지 판별
        return (square_root + 1)**2 # 정수가 맞다면 1을 더한 후 제곱
    else: # n의 제곱근이 이를 정수화한 값과 다르다면 
        return -1 