arr = input().split('-') # - 연산자 기준으로 입력 
num = [] # 합 리스트
for i in arr:
    cnt = 0
    s = i.split("+") # arr에서 + 연산자 기준으로 나눈다 
    for j in s:
        cnt += int(j) # 문자이므로 정수형으로 변환하여 더한다
    num.append(cnt) # 합 리스트에 추가
n = num[0] # 리스트 첫번째 값
for i in range(1, len(num)):
    n -= num[i] # 첫번째 값에서 합을 다 빼준다.
print(n)
    