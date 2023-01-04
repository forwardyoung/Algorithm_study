from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split())) # [10, 20, 10, 30, 20, 50]
dp = [] # 가장 긴 증가하는 부분 수열 [10, 20, 30, 50]

for i in arr:
    k = bisect_left(dp, i) # dp에 i가 들어갈 위치 (인덱스)
    if len(dp) <= k: # i가 가장 큰 숫자라면 (k가 dp 리스트의 맨 오른쪽에 위치할 때)
        dp.append(i) 
    else: # i가 dp의 최댓값보다 작다면
        dp[k] = i # dp에 대해 알맞은 위치(k)에 num을 대치
print(len(dp)) # dp(가장 긴 증가하는 부분 수열)의 길이 출력