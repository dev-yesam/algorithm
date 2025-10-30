# 온풍기 위치 때문에?
# 패딩 씌운거 때문에?


# 범위 이탈 여부 함수
def inarea(a, b):
    if 0 < a <= r and 0 < b <= c:
        return True
    else:
        return False


# 온풍기 바람 받는 함수
def prevtemp(a, b, direction):
    if direction == 1:  # 우측방향 온풍기
        straight = temper[a][b - 1]
        upright = temper[a + 1][b - 1] if walls_up[a + 1][b - 1] != 1 else 0
        downright = temper[a - 1][b - 1] if walls_up[a][b - 1] != 1 else 0
        return max(max(straight, upright, downright) - 1, 0)
    elif direction == 2:  # 좌측방향 온풍기
        straight = temper[a][b + 1]
        upleft = temper[a + 1][b + 1] if walls_up[a + 1][b + 1] != 1 else 0
        downleft = temper[a - 1][b + 1] if walls_up[a][b + 1] != 1 else 0
        return max(max(straight, upleft, downleft) - 1, 0)
    elif direction == 3:  # 위측방향 온풍기
        straight = temper[a + 1][b]
        rightup = temper[a + 1][b - 1] if walls_right[a + 1][b - 1] != 1 else 0
        leftup = temper[a + 1][b + 1] if walls_right[a + 1][b] != 1 else 0
        return max(max(straight, rightup, leftup) - 1, 0)
    else:  # 하측 방향 온풍기
        straight = temper[a - 1][b]
        rightdown = temper[a - 1][b - 1] if walls_right[a - 1][b - 1] != 1 else 0
        leftdown = temper[a - 1][b + 1] if walls_right[a - 1][b] != 1 else 0
        return max(max(straight, rightdown, leftdown) - 1, 0)


r, c, target = map(int, input().split())  # 행 크기, 열 크기, 기준온도
arr = [[-1] * (c + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(r)] + [[-1] * (c + 2)]
w = int(input())  # 벽 개수
walls_up = [[0] * (c + 2) for _ in range(r + 2)]
walls_right = [[0] * (c + 2) for _ in range(r + 2)]
for _ in range(w):
    # t가 0이면 해당 칸 위쪽에 벽, t가 1이면 해당 칸 우측에 벽.
    x, y, t = map(int, input().split())
    if t == 0:
        walls_up[x][y] = 1
    elif t == 1:
        walls_right[x][y] = 1

# 새로운 배열 만들어서 거기에 온도 정보를 둬야할 듯.
roomtemper = [[0] * (c + 2) for _ in range(r + 2)]

choco = 0
while choco <= 100:
    if choco == 100:
        choco = 101
        break

    # 1) 온풍기 바람 작용
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if arr[i][j] == 0 or arr[i][j] == 5:
                continue
            # 임시 온풍기 바람온도
            temper = [[0] * (c + 2) for _ in range(r + 2)]
            # 우측방향 온풍기
            if arr[i][j] == 1:
                temper[i][j + 1] += 5
                for k in range(1, 5):
                    for m in range(k * (-1), k + 1):
                        new_r, new_c = i + m, j + k + 1
                        # 범위를 벗어난 게 아니라면,
                        if not inarea(new_r, new_c):
                            continue
                        # 왼쪽 칸에 벽이 있다?
                        if walls_right[new_r][new_c - 1] == 1:
                            continue
                        # 온도 추가
                        temper[new_r][new_c] = prevtemp(new_r, new_c, 1)
            # 좌측 방향 온풍기
            elif arr[i][j] == 2:
                temper[i][j - 1] += 5
                for k in range(1, 5):
                    for m in range(k * (-1), k + 1):
                        new_r, new_c = i + m, j - 1 - k
                        # 범위를 벗어난 게 아니라면,
                        if not inarea(new_r, new_c):
                            continue
                        # 오른쪽 칸에 벽이 있다?
                        if walls_right[new_r][new_c] == 1:
                            continue
                        # 온도 추가
                        temper[new_r][new_c] = prevtemp(new_r, new_c, 2)
            # 상측 방향 온풍기
            elif arr[i][j] == 3:
                temper[i - 1][j] += 5
                for k in range(1, 5):
                    for m in range(k * (-1), k + 1):
                        new_r, new_c = i - 1 - k, j + m
                        # 범위 이탈 여부
                        if not inarea(new_r, new_c):
                            continue
                        # 아래쪽에 벽이 있다면?
                        if walls_up[new_r + 1][new_c] == 1:
                            continue
                        # 온도 추가
                        temper[new_r][new_c] = prevtemp(new_r, new_c, 3)
            # 하측 방향 온풍기
            elif arr[i][j] == 4:
                temper[i + 1][j] += 5
                for k in range(1, 5):
                    for m in range(k * (-1), k + 1):
                        new_r, new_c = i + 1 + k, j + m
                        # 범위 이탈 여부
                        if not inarea(new_r, new_c):
                            continue
                        # 위쪽에 벽이 있다면?
                        if walls_up[new_r][new_c] == 1:
                            continue
                        # 온도 추가
                        temper[new_r][new_c] = prevtemp(new_r, new_c, 4)
            # 방 온도 갱신
            for a in range(1, r + 1):
                for b in range(1, c + 1):
                    if temper[a][b]:
                        roomtemper[a][b] += temper[a][b]

    # 2) 온도 조절 과정
    controltemper = [[0] * (c + 2) for _ in range(r + 2)]
    # 2-1) 온도 비교
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            # 하 온도
            if i + 1 <= r and walls_up[i + 1][j] != 1:
                dif = roomtemper[i][j] - roomtemper[i + 1][j]
                if dif > 0:
                    controltemper[i][j] -= (dif // 4)
                    controltemper[i + 1][j] += (dif // 4)
                else:
                    dif *= -1
                    controltemper[i][j] += (dif // 4)
                    controltemper[i + 1][j] -= (dif // 4)
            # 우 온도
            if j + 1 <= c and walls_right[i][j] != 1:
                dif = roomtemper[i][j] - roomtemper[i][j + 1]
                if dif > 0:
                    controltemper[i][j] -= (dif // 4)
                    controltemper[i][j + 1] += (dif // 4)
                else:
                    dif *= -1
                    controltemper[i][j] += (dif // 4)
                    controltemper[i][j + 1] -= (dif // 4)
    # 2-2) 온도 조절
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            roomtemper[i][j] += controltemper[i][j]

    # 3) 온도가 1 이상인 가장 바깥쪽 온도가 1씩 감소
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if i == 1 or i == r:
                if roomtemper[i][j] > 0:
                    roomtemper[i][j] -= 1
            else:
                if j == 1 or j == c:
                    if roomtemper[i][j] > 0:
                        roomtemper[i][j] -= 1

    # 4) 초콜릿 먹기
    choco += 1

    # 5) 조사하는 모든 칸 target 온도 이상인지 검사
    flag = True  # 탈출 플래그
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if arr[i][j] == 5:
                if roomtemper[i][j] < target:
                    flag = False
    if flag:
        break

# for i in range(1,r+1):
#     print(roomtemper[i][1:c+1])

print(choco)
