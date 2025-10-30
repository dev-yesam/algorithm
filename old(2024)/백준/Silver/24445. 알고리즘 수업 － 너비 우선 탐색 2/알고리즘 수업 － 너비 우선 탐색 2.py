from collections import deque

n, m, r =map(int, input().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
for i in adjl:
    i.sort(reverse=True)
visited=[0]*(n+1)

def bfs(start):
    # 방문해서 할 일
    cnt = 1
    visited[start] = cnt
    cnt += 1
    q = deque()
    q.append(start)

    # 방문 예약
    while q:
        now = q.popleft()
        for next in adjl[now]:
            if not visited[next]:
                visited[next] = cnt
                cnt +=1
                q.append(next)

bfs(r)

for i in visited[1:]:
    print(i)