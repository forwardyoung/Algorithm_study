T = int(input())

for tc in range(1, T+1):
    numbers = input()
    numbers = numbers.split() # 띄어쓰기 기준으로 앞, 뒤로 자른다.       
    numbers = list(map(int, numbers)) # list로 숫자들을 담는다.
    
    n_numbers = []
    cnt = 0
    result = 0
    check = [0 for _ in range(10)]
    
    while True:
        for number in numbers:                          # ex) nubmers = [1295]
            cnt += 1
            n_numbers = cnt * number                    # ex) n_numbers = 1295 * 1 = 1295
            for i in map(int, str(n_numbers)):
                check[i] = 1                            # ex) i = 1, 2, 9, 5 // check[1] = 1 , check[2] = 1...
                
        if sum(check) == 10:                            # ex) check의 모든 리스트가 1이면 sum()이 10이므로, 종료.
            result = n_numbers 
            break
            
            
    print(f'#{tc} {result}')