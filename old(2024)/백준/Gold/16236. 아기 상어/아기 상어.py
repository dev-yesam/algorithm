from collections import deque


# 물고기 먹을 때마다 bfs 돌리면 되는 거같은데?
def bfs(r, c, big):
    # 시작점 처리 (재방문 않도록)
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    temp_lst = []

    # 방문 예약
    while q:
        # 꺼내기
        cr, cc = q.popleft()

        # 물고기냐?
        # 몇초 걸린지 리턴
        # 물고기 잡은 위치도 알아야 함.
        if 1 <= arr[cr][cc] < big:
            # 다음 방문 예약할 필요 없어짐
            temp_lst.append((visited[cr][cc], cr, cc))

            while q:
                # 꺼내기
                cr, cc = q.popleft()

                # 물고기냐?
                # 몇초 걸린지 리턴
                # 물고기 잡은 위치도 알아야 함.
                if 1 <= arr[cr][cc] < big:
                    temp_lst.append((visited[cr][cc], cr, cc))

            break

        # 다음 방문
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc

            # 범위 안 벗어났고, 방문 안했고, 큰 물고기 없다면
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and arr[nr][nc] <= big:
                visited[nr][nc] = visited[cr][cc] + 1
                q.append((nr, nc))


    if temp_lst:
        temp_lst.sort(key=lambda x: (x[0], x[1], x[2]))
        # print(temp_lst)
        return temp_lst[0][0] - 1, temp_lst[0][1], temp_lst[0][2]

    # while 다 돌렸는데 물고기 못먹었다?
    return -10, -10, -10


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 아기 상어 위치,
r = c = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            r, c = i, j

# 1마리씩 먹어보자.
cnt = 0  # 걸린 시간
big = 2  # 처음 아기 상어 크기
eaten_fish = 0  # 그 크기일 때 물고기 먹은 수
while True:

    visited = [[0] * n for _ in range(n)]
    arr[r][c] = 0  # 상어 있던 위치는 0으로 바꿔주기.

    # print(f"현재 진행 상항 cnt : {cnt}")
    # for i in arr:
    #     print(i)


    temp, next_r, next_c = bfs(r, c, big)

    # 새로 물고기 못잡았다면 break
    # 시간 더 줄이려며 물고기 수 미리 세기
    if temp == -10:
        break




    # print(f"잡은 물고기 & 물고기 크기 : {eaten_fish + 1}&{big}")
    # # 물고기 잡았다면?
    # # 물고기 잡은 수가, 크기와 같아지면 레벨업
    # # print(f"eaten_fish: {eaten_fish}")
    # print("=============")
    eaten_fish += 1
    if eaten_fish == big:
        big += 1
        eaten_fish = 0

    # 새로 물고기 잡은 위치로 넣어야함.
    r, c = next_r, next_c

    # 물고기 잡는데 걸린 시간,
    cnt += temp

    # print(f"잡은 물고기 좌표 {(r, c)}, 소요시간 : {cnt}")

print(cnt)
