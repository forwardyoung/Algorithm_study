def solution(n):
    square_root = n**(1/2)
    
    if int(square_root) == square_root:
        return (square_root + 1)**2
    else:
        return -1