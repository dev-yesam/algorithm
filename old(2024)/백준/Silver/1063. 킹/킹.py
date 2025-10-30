
# 알파벳: 열, 숫자: 행

# 입력
king_loc, stone_loc, N = input().split()
N = int(N)

# 행렬 말고, xy 좌표 개념으로 계산
# 현재 위치 (1,a)를 (0,0)으로 계산.
kx = ord(king_loc[0]) - 65
ky = int(king_loc[1]) - 1

sx = ord(stone_loc[0]) - 65
sy = int(stone_loc[1]) - 1

# 델타 우좌하상/ 우상 좌상 우하 좌하
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, - 1]

# 움직임 명령어들
dirs = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']


# 체스판 안에 있는지 여부 함수
def in_area(x, y):
    return 0 <= x < 8 and 0 <= y < 8


# 움직임 함수
def move(x, y, d):
    global sx, sy
    nx = x + dx[d]
    ny = y + dy[d]

    # 영역 내 여부
    if in_area(nx, ny):

        # 돌이 있는지 여부
        if (nx, ny) == (sx, sy):
            sx,sy = move(sx, sy, d)  # 돌을 옮겨

            # 돌이 안 옮겨졌다?
            if (nx, ny) == (sx, sy):
                pass
            # 돌이 옮겨졌다?
            else:
                x, y = nx, ny

        else:
            x, y = nx, ny

    return x, y  # 재할당 해야 함


# 명령어 입력 및 실행
for _ in range(N):
    dir = input()

    d = dirs.index(dir)
    kx, ky = move(kx, ky, d)

# 왕과 돌 위치 출력
kx, ky = chr(kx + 65), str(ky + 1)
sx, sy = chr(sx + 65), str(sy + 1)

print(kx, ky, sep='')
print(sx, sy, sep='')
