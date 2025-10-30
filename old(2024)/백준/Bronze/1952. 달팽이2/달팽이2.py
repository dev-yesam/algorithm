# 입력
m, n = map(int, input().split())

# 어레이 입력
arr = [[0] * n for _ in range(m)]

# 달팽이 현재 위치
r, c = 0, 0

# 달팽이 이동 방향
d = 0  # 처음 우측 진행

# 달팽이 이동: 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 꺾이는 횟수
cnt = 0

# 달팽이 이동
for _ in range(m * n - 1):

    # 현재 위치 수정 (재방문 않도록)
    arr[r][c] =1

    # 이동 위치
    nr = r + dr[d]
    nc = c + dc[d]

    # 이동 가능 여부 확인
    if 0 <= nr < m and 0 <= nc < n and arr[nr][nc] == 0:

        # 이동
        r, c = nr, nc

    else:  # 방향 전환 및 이동
        d = (d + 1) % 4
        r = r + dr[d]
        c = c + dc[d]
        cnt +=1

# 출력
print(cnt)
