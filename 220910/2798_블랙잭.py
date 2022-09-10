n, m = map(int,(input().split()))

num = list(map(int, input().split())) # 카드 숫자 리스트

result = 0
Max = 0

for i in range(n-2): # 3중 for문을 돌면서 겹치지 않게 범위를 지정
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if num[i]+num[j]+num[k] > m: # 3개의 값 더한것이 m보다 크다면 넘어감
                continue
            else:
                result = num[i]+num[j]+num[k]
                if Max <= result: # m과 가장 유사한 값은 가장 큰 값이기 때문에 비교해서 큰값을 저장
                    Max = result

print(Max)