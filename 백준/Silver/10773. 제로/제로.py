import sys
input = sys.stdin.readline # 시간 초과 방지

K = int(input())
stack = [] # stack 리스트 생성
for i in range(K): # K번 순회하는 반복문
    num = int(input()) # K개 줄에 정수 입력 받음
    if num == 0: # 입력받은 수가 0이면
        stack.pop() # 가장 최근에 쓴 수 지우고
    else: # 입력 받은 수가 0이 아니면
        stack.append(num) # stack 리스트에 추가
print(sum(stack)) # stack 리스트에 남은 수의 합 
    