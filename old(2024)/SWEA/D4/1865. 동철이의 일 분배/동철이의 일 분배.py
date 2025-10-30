def recur(level, cnt):
    global total

    # 가지 치기
    if cnt <= total:
        return

    # 종료 조건
    if level == n:
        # 어떤 값 내놓아야함.
        total = max(total, cnt)
        return

    # 재귀호출
    for i in range(n):
        if not col_visited[i]:
            col_visited[i] = 1
            recur(level + 1, cnt * arr[level][i])
            col_visited[i] = 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] *= 0.01

    # 열마다 1번만 해야함
    col_visited = [0] * n
    total = 0
    recur(0, 1)

    print(f'#{tc} {100 * total:.6f}')
