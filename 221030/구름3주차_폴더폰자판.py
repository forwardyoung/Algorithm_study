import sys
input = sys.stdin.readline

n = int(input()) # 수열의 길이
dic = {
    1 : "1.,?!",
    2 : "2ABC",
    3 : "3DEF",
    4 : "4GHI",
    5 : "5JKL",
    6 : "6MNO",
    7 : "7PQRS",
    8 : "8TUV",
    9 : "9WXYZ",
}
s = input() # 수열 s
ans = ''
cnt = 0
for i in range(n):
    if i == n:
        break
    else:
        if s[i+1] == s[i]:
            cnt += 1
            continue
        else:
            cnt %= len(dic[int(s[i])])
            ans += dic[int(s[i])][cnt]
            cnt = 0
print(ans)