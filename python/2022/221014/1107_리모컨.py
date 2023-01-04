N = int(input()) # 채널 번호
ans = abs(100 - N) # ++, -- 로 이동할 경우 -> 최댓값
M = int(input()) # 고장난 버튼의 수 
if M: # 고장났다면 
    broken = set(input().split()) # 고장난 버튼 입력 받는다. 
else:
    broken = set()

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001): 
    for N in str(num):
        if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - N))

print(ans)