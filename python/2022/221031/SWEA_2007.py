T = int(input())
for test_case in range(1, T + 1):
    s=input()
    for j in range(1,10):
        if s[:j]==s[j:2*j]:
            print(f'#{test_case} {j}')
            break