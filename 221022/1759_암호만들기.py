L, C = map(int, input().split()) # 암호는 서로 다른 L개의 알파벳으로 구성, 암호로 고를 수 있는 알파벳 C개
char = list(input().split()) # 무심코 map(int, input().split())을 쓰고 있다. 주의!
char.sort() # 알파벳 정렬 ['a', 'c', 'i', 's', 't', 'w']

vowel = ['a', 'e', 'i', 'o', 'u'] # 암호는 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성

ans = []
visited = [0] * C

def is_vowel(ans): # 모음 포함 여부
    for i in range(len(vowel)):
        if vowel[i] in ans:
            return 1
    return 0

def is_two_cons(ans): # 자음 2개 포함 여부
    cnt = 0
    for i in range(len(ans)):
        if ans[i] not in vowel: # 모음이 아니면 cnt를 1 더한다 = 자음
            cnt += 1
    if cnt >= 2:
        return 1
    else:
        return 0

def dfs(iter):
    if len(ans) == L:
        if is_vowel(ans) and is_two_cons(ans): # 모음 1개 이상, 자음 2개 이상
            print(''.join(ans))
            return
    for i in range(iter, C):
        if not visited[i]:
            ans.append(char[i])
            visited[i] = 1
            dfs(i)
            visited[i] = 0
            ans.pop()
dfs(0)