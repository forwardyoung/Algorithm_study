def solution(sizes):
    answer = 0

    sizes = [sorted(size, reverse=True) for size in sizes]

    width = [size[0] for size in sizes]
    height = [size[1] for size in sizes]

    w, h = max(width), max(height)

    answer = w*h

    return answer

# 간단한 풀이
# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)

