def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i) # stack 리스트에 '(' 추가
        else: # i가 닫힌 괄호 ')'라면
            if stack == []: # 꺼낼 문자가 없다면
                return False # False 값을 리턴
            else:
                stack.pop() # stack 리스트의 '(' 문자를 하나 꺼내고
    return len(stack) == 0 # 꺼낼 문자열이 없다면 => 올바른 괄호면 True 리턴