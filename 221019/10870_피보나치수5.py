def fibo(n):
    if n <= 1: # n이 0일 때는 0, n이 1일 때는 1이므로 n <= 1일때는 n을 반환
        return n
    return fibo(n-1) + fibo(n-2) # 피보나치 수는 앞 두 수의 합

n = int(input())
print(fibo(n))