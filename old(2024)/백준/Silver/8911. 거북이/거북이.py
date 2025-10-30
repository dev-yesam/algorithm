# x좌표 최대 최소의 차 * y 좌표의 최대 최소의 차
# 델타 배열


t = int(input())
for _ in range(t):
    cmd = list(input())

    x, y = 0, 0  # 현위치
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    d = 0
    Mx, mx = 0, 0
    My, my = 0, 0

    # 명령어 실행
    for c in cmd:

        if c == 'F':
            x += dx[d]
            y += dy[d]
            Mx, mx = max(Mx, x), min(mx, x)
            My, my = max(My, y), min(my, y)

        elif c == 'B':
            x -= dx[d]
            y -= dy[d]
            Mx, mx = max(Mx, x), min(mx, x)
            My, my = max(My, y), min(my, y)

        elif c == 'L':
            d = (d - 1) % 4

        elif c == 'R':
            d = (d + 1) % 4


    print((Mx-mx)*(My-my))