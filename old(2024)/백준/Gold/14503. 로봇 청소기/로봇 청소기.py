# 로봇 청소기
# 방 상태

# [1]
# 현재 칸 청소 안됐으면 현재 칸 청소 => 처음만하면 됨.
# 주변 4칸 깨끗하면 1칸 후진하고  -> 후진 못하면(벽) 종료

# [2]
# 주변 4칸 중 청소해야 하면 반시계(왼쪽) 90도 회전
# 앞에 청소해야하는 빈칸이면 1칸 전진 후 청소. 아니면 다시 왼쪽 90도 회전

# [출력] 청소한 칸의 수

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d0~3 방향 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

arr = [list(map(int, input().split())) for _ in range(N)]
# 0 : 청소 안된 칸( 처음 빈칸은 전부 청소안된거임)
# 1 : 벽
# 2 : 청소 된 칸 (임의 지정해봄)


# 초기 위치 청소
arr[r][c] = 2
cnt = 1

# 칸 개수 세기
while True:
    # 4칸 중 청소 안된 칸 여부
    is_clean = True  # 기본값 깨끗한 것
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            is_clean = False

    # [1] 청소 안된 칸이 없다
    if is_clean:
        # 1칸 후진
        nr, nc = r - dr[d], c - dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1:
            r, c = nr, nc
            continue
        # 후진 하지 못한다면
        else:
            break


    # [2] 청소 안된 칸이 있다
    else:
        for _ in range(4):
            d = (d - 1) % 4
            # 앞쪽 칸이 청소가 안되어 있다면?
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                r, c = nr, nc
                arr[r][c] = 2
                cnt += 1
                break

print(cnt)
