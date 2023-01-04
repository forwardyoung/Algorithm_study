T = int(input())
for i in range(1, T+1): # 1 ~ 100

    i = str(i) # 다음 코드에서 count를 하기 위해 int형의 i를 str으로 형변환
    
    clap = i.count('3') + i.count('6') + i.count('9') # 박수 횟수를 clap이라는 변수에 

    if clap == 0:
        print(i, end=' ')
    else:
        print("-" * clap, end=' ') # 박수 횟수에 맞게 "-"를 출력