## for문을 다 돌기도 전에 return 하면 이꼴이 난다~
## for문에서 continue, break, return에서 실수가 잦은 듯함
# 사실 백트래킹에서 새로운 가지에 대한 이해 부족인듯. => 백트 개념 공부하면 될듯.

from collections import deque

def recur(level, start, y_num):
    global cnt
    # 조합
    if level == 7:
        for i in range(5):
            for j in range(5):
                if cmb[i][j] == 1:
                    if bfs(i, j) == 7:
                        cnt += 1
                    return
        return

    # 다음 조합 원소
    for next in range(start, 25):
        # 임도연 파?
        if arr[next // 5][next % 5] == 'Y':
            if y_num + 1 >= 4:
                continue
            cmb[next // 5][next % 5] = 1
            recur(level + 1, next + 1, y_num + 1)
            cmb[next // 5][next % 5] = 0
        # not 임도연 파?
        else:
            cmb[next//5][next%5] = 1
            recur(level + 1, next + 1, y_num)
            cmb[next//5][next%5] = 0


def bfs(r, c):
    # 시작점 처리
    seven_num = 1
    visited = [[0] * 5 for _ in range(5)]
    visited[r][c] = 1
    q = deque()
    q.append((r, c))

    while q:
        cr, cc = q.popleft()

        for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and cmb[nr][nc]:
                visited[nr][nc] = 1
                seven_num += 1
                q.append((nr, nc))

    return seven_num


arr = [input() for _ in range(5)]

cmb = [[0]*5 for _ in range(5)]
cnt = 0

# cmb = [[0,0,0,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
# for i in range(5):
#     for j in range(5):
#         if cmb[i][j] == 1:
#             if bfs(i, j) == 7:
#                 cnt += 1
recur(0, 0, 0)
print(cnt)

