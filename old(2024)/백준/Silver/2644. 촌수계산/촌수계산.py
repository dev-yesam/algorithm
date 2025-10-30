from collections import deque

# n 사람 수
n = int(input())
# 촌수 계산할 사람 번호
start, goal = map(int, input().split())
# 관계 개수 및 그래프
m = int(input())
adjl = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

visited = [-1] * (n + 1)


def bfs(start, goal):
    # 방문 처리
    visited[start] = 0
    q = deque()
    q.append(start)

    # 예약 방문 처리
    while q:
        now = q.popleft()
        for next in adjl[now]:
            if visited[next] < 0:
                visited[next] = visited[now] + 1
                q.append(next)
                # 종료조건
                if next == goal:
                    return visited[next]

    return -1


print(bfs(start, goal))
