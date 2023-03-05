N = int(input())

def solve(start, stack):
    if start == N + 1:
        return [list(reversed(stack))]

    ret = []

    if len(stack) != 0:
        last = stack.pop()
        next = solve(start, stack)
        ret += [[last] + x for x in next]
        stack.append(last)

    stack.append(start)
    ret += solve(start + 1, stack)
    stack.pop()

    return ret

for ans in solve(1, []):
    print(*ans)