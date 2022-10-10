n, k = map(int, input().split())
list_ = []
for _ in range(n):
	word = input()
	list_.append(word)
list_.sort()
list_.sort(key = lambda x : len(x)) # 이 코드가 없다면 list_ = ['a', 'aa', 'aaa', 'aaaa', 'b', 'bb', 'bbb']
# print(list_) ['a', 'b', 'aa', 'bb', 'aaa', 'bbb', 'aaaa']
print(list_[k-1])