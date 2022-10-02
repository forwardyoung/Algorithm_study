T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 뿔의 개수, M : 전체 동물의 수
    # x : 트윈혼의 수, y : 유니콘의 수
    # x + y = M
    # y = M - x 
    # 트윈혼은 뿔이 2개이므로 트윈혼의 수*2가 트윈혼 전체 뿔의 수
    # 2x + y = N, 위의 식을 y에 대입하면 2x + M - x = N
    # x + M = N
    x = N - M # x : 트윈혼의 수 
    y = M - x # 위에서 구한 트윈혼의 수를 전체 동물의 수에서 빼준다.

    print("#{} {} {}".format(tc, y, x)) # 유니콘을 먼저 출력해야 하므로 y, x 순