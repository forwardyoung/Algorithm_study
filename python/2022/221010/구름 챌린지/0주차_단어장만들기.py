n, k = map(int, input().split())
list_ = []
for _ in range(n):
	word = input()
	list_.append(word)
list_.sort()
list_.sort(key = lambda x : len(x)) # 이 코드가 없다면 list_ = ['a', 'aa', 'aaa', 'aaaa', 'b', 'bb', 'bbb']
# print(list_) ['a', 'b', 'aa', 'bb', 'aaa', 'bbb', 'aaaa']
print(list_[k-1])

# 해설 코드
# word = list()
# n, k = map(int, input().split())
# for i in range(n):
#     word.append(input().rstrip()) # rstrip()을 사용해 입력 받은 단어들을 공백 없이 리스트에 담는다.
# print(word)