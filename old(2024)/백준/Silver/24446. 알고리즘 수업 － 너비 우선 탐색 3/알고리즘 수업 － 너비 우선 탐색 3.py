from collections import deque

n,m,r = map(int,input().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adjl[a].append(b)
    adjl[b].append(a)

visited= [-1] * (n+1)

def bfs(start):
    # 시작 처리
    visited[start] = 0
    q = deque()
    q.append(start)

    # 예약 방문
    while q:
        now = q.popleft()

        for next in adjl[now]:
            if visited[next] < 0:
                visited[next] = visited[now] + 1
                q.append(next)

bfs(r)

for i in visited[1:]:
    print(i)