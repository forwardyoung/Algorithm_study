a, b = map(int, input().split())
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1): # b가 이기면
    print("B")
else: # a가 이기면
    print("A")
