t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    # 맨 왼쪽 맨 위가 1,1로 시작함
    arr = [[0] * (n + 2) for _ in range(n + 2)]  # 패딩 추가
    arr[n // 2 + 1][n // 2] = arr[n // 2][n // 2 + 1] = 1  # 흑돌
    arr[n // 2][n // 2] = arr[n // 2 + 1][n // 2 + 1] = 2  # 백돌
    for _ in range(m):
        c, r, stone = map(int, input().split())
        arr[r][c] = stone

        # 상 하 좌 우/ 좌상 우상 좌하 우하/ 살펴서...
        dc = [0, 0, -1, 1, -1, 1, -1, 1]
        dr = [-1, 1, 0, 0, -1, -1, 1, 1]
        for d in range(8):
            can_lst = []
            for move in range(1, n):
                nc, nr = c + dc[d] * move, r + dr[d] * move
                if arr[nr][nc] == 0:
                    break
                elif arr[nr][nc] != stone:
                    can_lst.append((nr, nc))
                else:
                    for can in can_lst:
                        arr[can[0]][can[1]] = stone
                    break

    w_num = b_num = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]== 1:
                b_num += 1
            elif arr[i][j] == 2:
                w_num += 1

    print(f'#{tc}', b_num, w_num)