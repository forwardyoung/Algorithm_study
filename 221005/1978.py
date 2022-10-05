N = int(input())
num = list(map(int, input().split())) # N개의 숫자들을 입력받는다.
ans = 0 # 소수의 개수

for i in num: # 입력 받은 num을 하나씩 순회
    cnt = 0
    if i ==1: # i가 1이라면 처음으로
        continue
    for j in range(2, i+1): # 소수는 1과 자기 자신만으로 나눠진다.
        if i%j == 0: 
            cnt += 1
    if (cnt == 1): # cnt가 1이라면 소수이므로
        ans += 1 # 소수의 개수에 1을 더한다.
print(ans)
