def solution(priorities, location):
    # 1. Queue를 만든다.
    printer = [(i, p) for i, p in enumerate(priorities)]
    turn = 0
    while printer:
        work = printer.pop(0)
        # 2. 나보다 중요한 작업이 있으면 뒤에 넣는다.
        if any(work[1] < other_work[1] for other_work in printer):
            printer.append(work)
        else:
            turn += 1
            # 3. 내가 제일 중요하다면 수행하고 location과 비교한다.
            if work[0] == location:
                break
    return turn

    
print(solution([1, 1, 9, 1, 1, 1], 0))