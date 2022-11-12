# 쇠막대기 자르기 문제
T = int(input())
for tc in range(1,T+1):
    lst = list(input())
    stick = 0
    cnt = 0
    l = len(lst)
    i = 0
    while i < l:
        # ( 다음에 바로 ')' 가 나온다면 레이저 
        if lst[i] == '(' and lst[i+1]==')':
            cnt += stick
            i += 2
        # 바로 다음에 )가 나오지 않는 '(' 라면 쇠막대기
        elif lst[i] == '(':
            stick += 1
            i += 1
        # 나머지는 레이저가 아닌 ')'로 쇠막대기의 끝이다. cnt 값 1을 증가시키고 쇠막대기 개수를 1 낮춘다.
        else:
            cnt += 1
            stick -= 1
            i += 1
    print('#{} {}'.format(tc,cnt))