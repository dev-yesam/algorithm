import sys

n, m, r = map(int, input().split())
sys.setrecursionlimit(n + 10)

adjl = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
for node in adjl:
    node.sort(reverse=True)


def dfs(now, cnt):
    global visit_order, total
    visit_order += 1
    visited[now] = cnt * visit_order

    total += visited[now]

    for next in adjl[now]:
        if visited[next] == -1:
            dfs(next, cnt + 1)


total = visit_order = 0
dfs(r, 0)

print(total)