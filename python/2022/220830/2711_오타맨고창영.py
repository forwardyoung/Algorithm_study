T = int(input())
for _ in range(T):
    l, w = input().split()
    list_ = list(w)
    list_.pop(int(l)-1) # pop(i) 함수는 리스트에서 주어진 위치(인덱스)에 있는 요소를 삭제하고, 그 요소를 반환
    # l은 str으로 입력 받았기 때문에 int로 형변환 후에 1을 빼야 한다!
    # print(list_) ['M', 'I', 'S', 'P', 'E', 'L', 'L']
    print("".join(list_))

# 틀린 풀이 (마지막 print문)
#     for i in list_:
#         print(i, end="")
# 출력 결과가 다음과 같다.
# MISPELL1 PROGRAMMING
# ROGRAMMING7 CONTEST