T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split()) # 현미빵 : A원, 단호박빵 : B원, 은비 잔고 : C원
    ans = C // min(A, B) # A, B 둘 중 더 값싼 빵으로 은비의 잔고를 나눈다. 
    print(f"#{tc} {ans}")
