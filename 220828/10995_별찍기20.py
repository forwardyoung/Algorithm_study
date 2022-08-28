N = int(input())
for i in range(1, N+1):
    if i%2 == 1: # i가 홀수이면
        print('* ' * N) # 맨 앞글자가 *부터 시작
    else: # i가 짝수이면
        print(' *' * N) # 맨 앞글자가 공백부터 시작