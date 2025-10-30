x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def cww(a1, b1, a2, b2, a3, b3):
    result = (a1 * b2 - b1 * a2) + (a2 * b3 - b2 * a3) + (a3 * b1 - a1 * b3)
    if result > 0:
        return 1  # CWW
    else:
        return -1  # CW


ans1 = cww(x1, y1, x2, y2, x3, y3) * cww(x1, y1, x2, y2, x4, y4)
ans2 = cww(x3, y3, x4, y4, x1, y1) * cww(x3, y3, x4, y4, x2, y2)
if ans1 == -1 and ans2 == -1:
    print(1)
else:
    print(0)
