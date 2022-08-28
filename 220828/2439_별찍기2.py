N = int(input())
for i in range(1, N+1): # i는 1부터 N까지
    print(' '*(N-i) + '*'*i) # 먼저 i가 1이라면 공백이 네 칸이어야 하므로 N-i(5-1)을 하고 1개의 *를 더한다.