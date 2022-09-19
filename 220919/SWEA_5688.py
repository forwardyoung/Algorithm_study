# 풀이 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = round(pow(N, 1/3))  # pow(x, y) x의 y제곱 / round : 반올림

    if result**3 == N:
        print('#%d %d' % (tc, result))
    else:
        print('#%d %d' % (tc, -1))

# 풀이 2
# T = int(input())
	
# for tc in range(1, T+1):
#     N = int(input())
#     X = round(N**(1/3))
#     result = X
#     if X ** 3 != N:
#         result = -1

#     print(f'#{tc} {result}')