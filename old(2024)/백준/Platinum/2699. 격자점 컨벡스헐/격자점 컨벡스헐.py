def ccw(a, b, c):
    return (a[0] * b[1] - a[1] * b[0]) + (b[0] * c[1] - b[1] * c[0]) + (c[0] * a[1] - c[1] * a[0])


t = int(input())
for _ in range(t):
    n = int(input())
    rotation_n = (n - 1) // 5 + 1
    lst = []
    for _ in range(rotation_n):
        coords = list(map(int, input().split()))
        coords_n = len(coords)
        for i in range(coords_n // 2):
            lst.append((coords[2 * i], coords[2 * i + 1]))

    # 0일때도 포함
    lst.sort(key=lambda x: (-x[1], x[0]))
    temp_cw = []
    temp_ccw = []

    # 모노톤 체인 상반부(시계방향)
    for i in lst:
        while True:
            if len(temp_cw) < 2:
                temp_cw.append(i)
                break
            if ccw(temp_cw[-2], temp_cw[-1], i) < 0:
                temp_cw.append(i)
                break
            else:
                temp_cw.pop()

    # 모노톤 체인 하반부 (반시계)
    for i in lst:
        while True:
            if len(temp_ccw) < 2:
                temp_ccw.append(i)
                break
            if ccw(temp_ccw[-2], temp_ccw[-1], i) > 0:
                temp_ccw.append(i)
                break
            else:
                temp_ccw.pop()

    convex_hull = temp_cw + temp_ccw[-2:0:-1]
    print(len(convex_hull))
    for i in convex_hull:
        print(*i)
