

from collections import deque


def bfs(i, j, rain):
    # 시작점 방문 처리
    visited[i][j] = 1
    q = deque()
    q.append((i, j))

    # 방문 예약
    while q:
        now = q.popleft()

        # 상하좌우
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = now[0] + di, now[1] + dj
            # 연결된 지역이면서, 방문하지도 않았고, 물에 잠기지 않았다면
            if 0<= ni < N and 0<= nj < N and not visited[ni][nj] and arr[ni][nj] > rain:
                visited[ni][nj] = 1
                q.append((ni,nj))

# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_rain = 100
max_rain = 1
for i in range(N):
    min_rain = min(min_rain, min(arr[i]))
    max_rain = max(max_rain, max(arr[i]))


# 강수량 마다 BFS 돌려서 개수 세기 => 최대 개수
ans = 0
for rain in range(min_rain-1, max_rain): # 아오 하나도 안 잠기는 것도 고려해야함
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] - rain > 0 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j, rain)

    ans = max(ans, cnt)

# 출력
print(ans)



##########################3
# N 지역 크기 N * N
# 높이 <= 강수량 : 물에 잠김
# 물에 잠기지 않은 영역의 개수 -> dfs,bfs 써서 인접한 애들 0으로 만들면 됨.

# 문제는 강수량은 최소 높이~ 최대 높이까지임.
