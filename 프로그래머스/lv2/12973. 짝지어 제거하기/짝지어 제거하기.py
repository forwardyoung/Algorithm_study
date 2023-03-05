def solution(s):
    stack = []
    for letter in s:
        if not stack: # if letter not in stack과 같은 의미
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