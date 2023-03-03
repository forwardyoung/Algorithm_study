def solution(s):
    stack = []
    for letter in s:
        if not stack:
            stack.append(letter)
        else:
            if stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
                
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer