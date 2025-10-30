from collections import deque

# F 건물 층 수
# S 현재 있는 층
# G 찾는 장소
# S -> G 로 엘베타고 이동해야함.
# U: 위로 U층 이동 (범위 넘으면 안 움직임)
# D: 아래로 D층 이동

# 최소 몇 번 눌러야 도착하는가? 도착할 수 없다면 "use the stairs" 출력

# 백트래킹 써서 조사. 가지치기로 숫자 많으면 쳐내면 될 듯 => 걍 BFS 씀.

F, S, G, U, D = map(int, input().split())


def bfs():
    visited = [0] * (F + 1)
    # 시작점 방문
    visited[S] = 1
    q = deque()
    q.append(S)

    # 방문 예약
    while q:
        now = q.popleft()
        if now == G:
            return visited[now] - 1
        for move in [U, D * (-1)]:
            next = now + move
            if 1 <= next <= F and not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)

    # 못 간다면
    return "use the stairs"

# 출력
print(bfs())
