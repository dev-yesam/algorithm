from collections import deque

n, m , r = map(int, input().split())

adjl = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for i in adjl:
    i.sort()

# 방문순서
visited = [0] * (n+1)
depth = [-1] * (n+1)

# bfs
def bfs(start):
    # 시작 방문 처리
    cnt =1
    visited[start] = cnt
    cnt += 1
    depth[start] = 0

    q= deque()
    q.append(start)

    # 예약 방문 처리
    while q:
        now = q.popleft()

        for next in adjl[now]:
            if not visited[next]:
                visited[next] = cnt
                cnt += 1
                depth[next] = depth[now]+1

                q.append(next)

bfs(r)
total = 0
for i in range(1,n+1):
    total += visited[i] *depth[i]


print(total)